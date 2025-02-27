def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if '0' in s:
            continue
        flag = True
        while len(s) > 1:
            if not is_prime(int(s)):
                flag = False
                break
            s = s[1:-1]
        if flag and is_prime(int(s)):
            primes.append(i)
    return primes