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

    def is_truncatable_left_right_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                return False
        return True
    x = numbers[29]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_left_right_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)