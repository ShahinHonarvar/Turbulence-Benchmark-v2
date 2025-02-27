def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = n[77]
    primes = []
    for i in range(x, 0, -1):
        s = str(i)
        if '0' in s or not is_prime(int(s)):
            continue
        while len(s) > 1:
            if not is_prime(int(s[1:-1])):
                break
            s = s[1:-1]
            if len(s) == 1:
                primes.append(i)
                break
    return sorted(primes, reverse=True)