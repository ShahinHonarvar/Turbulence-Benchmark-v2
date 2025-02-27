def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(prime):
        s = str(prime)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[89]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)