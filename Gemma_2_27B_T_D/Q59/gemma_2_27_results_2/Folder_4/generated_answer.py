def all_left_truncatable_prime(t):
    x = t[96]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if '0' not in s:
            is_prime = True
            for j in range(len(s)):
                if not is_prime:
                    break
                num = int(s[j:])
                if num < 2 or (num % 2 == 0 and num > 2):
                    is_prime = False
                for k in range(3, int(num ** 0.5) + 1, 2):
                    if num % k == 0:
                        is_prime = False
                        break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)