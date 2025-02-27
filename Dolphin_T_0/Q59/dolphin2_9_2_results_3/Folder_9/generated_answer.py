def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[29]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            s = str(i)
            if '0' in s:
                continue
            while s:
                if not is_prime(int(s)):
                    break
                if len(s) == 1:
                    primes.append(i)
                    break
                s = s[1:]
    return sorted(primes, reverse=True)