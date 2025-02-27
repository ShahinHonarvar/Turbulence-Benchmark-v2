def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable_prime(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(length):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = numbers[14]
    left_truncatable_primes = []
    for n in range(2, x):
        if '0' not in str(n) and is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return left_truncatable_primes