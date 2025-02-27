def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def left_right_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    x = numbers[33]
    truncatable_primes = []
    for num in range(10, x + 1):
        if left_right_truncatable(num) and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)