def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[98]
    ret_list = []
    for i in range(2, x):
        prime = True
        n = i
        while prime and n // 10 > 0:
            prime = is_prime(n)
            n //= 10
        if prime and n <= 9:
            ret_list.append(i)
    return sorted(ret_list)