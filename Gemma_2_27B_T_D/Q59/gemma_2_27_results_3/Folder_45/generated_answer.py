def all_left_truncatable_prime(numbers):
    x = numbers[61]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        s = str(i)
        if '0' not in s and is_prime(i):
            flag = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes)