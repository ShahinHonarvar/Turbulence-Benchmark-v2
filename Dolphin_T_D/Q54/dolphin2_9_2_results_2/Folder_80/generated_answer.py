def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_right_truncatable_prime(t):
    x = t[14]
    prime_set = set()
    for i in range(0, x - 1):
        if is_prime(i):
            prime_set.add(i)
    result = []
    for i in prime_set:
        if str(i) == str(i)[::-1] and str(i) != str(i)[-2:]:
            result.append(i)
    result.sort(reverse=True)
    return result