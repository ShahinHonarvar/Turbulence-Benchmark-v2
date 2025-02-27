def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = 1201726217
    l = []
    for i in range(1, x):
        s = str(i)
        if s[0] == '0':
            continue
        if is_prime(i):
            prime = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    prime = False
                    break
            if prime:
                l.append(i)
    return sorted(l)