def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(lst):
    x = lst[630]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if '0' not in s:
            while len(s) > 1:
                if not is_prime(int(s)):
                    break
                s = s[1:-1]
            else:
                primes.append(i)
    return sorted(primes, reverse=True)