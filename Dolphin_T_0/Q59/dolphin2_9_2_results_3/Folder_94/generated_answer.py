def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[43]
    prime = []
    for i in range(x):
        s = str(i)
        n = i
        while len(s) > 0 and n > 1 and is_prime(n):
            if is_prime(int(s)):
                prime.append(int(s))
            s = s[1:]
            n = int(s)
    return list(set(prime))