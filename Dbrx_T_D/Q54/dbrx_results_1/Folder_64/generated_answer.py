def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[4]
    rtp = []
    for i in range(1, 10):
        if is_prime(i):
            rtp.append(i)
    for i in range(1, len(str(x))):
        temp = [j for j in rtp if str(j).endswith(str(i))]
        rtp = [k for k in temp if is_prime(k)]
    return sorted(rtp)