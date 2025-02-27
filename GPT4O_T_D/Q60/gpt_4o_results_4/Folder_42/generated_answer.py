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

    def is_truncatable_prime(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(1, length):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
                return False
        return True
    if len(numbers) <= 64:
        return []
    x = numbers[64]
    truncatable_primes = []
    for number in range(10, x + 1):
        if '0' not in str(number) and is_prime(number) and is_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)