def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[39]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            for _ in range(1, len(s)):
                if not is_prime(int(s)):
                    break
                s = s[1:]
            else:
                primes.append(i)
    return sorted(primes)