def all_left_right_truncatable_prime(t):
    x = t[41]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if '0' not in s:
            is_prime = True
            for j in range(len(s)):
                if not (int(s[j:]) in [2, 3, 5, 7] or int(s[:j + 1]) in [2, 3, 5, 7]):
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)