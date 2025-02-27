def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        s = str(num)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[36]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)