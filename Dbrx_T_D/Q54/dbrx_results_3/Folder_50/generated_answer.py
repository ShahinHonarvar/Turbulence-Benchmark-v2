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
    x = tuple((i for i in t[56]))
    rtp = []
    for i in range(10, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num = remove_last_digit(num)
            else:
                rtp.append(i)
    return sorted(rtp, reverse=True)