def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = input_tuple[30]
    primes = []
    for i in range(1, x):
        if is_prime(i):
            s = str(i)
            while s:
                if not is_prime(int(s)):
                    break
                s = s[:-1]
            else:
                primes.append(i)
    return sorted(primes)