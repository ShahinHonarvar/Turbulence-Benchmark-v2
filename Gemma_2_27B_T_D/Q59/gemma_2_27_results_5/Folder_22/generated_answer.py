def all_left_truncatable_prime(t):
    x = t[85]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            flag = True
            for j in range(len(s)):
                if not is_prime(int(s[j:])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes)