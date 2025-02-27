def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[429]
    lrtp = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            n = i
            while n > 0:
                n = int(str(n)[1:])
                if n > 0 and (not is_prime(n)):
                    break
            else:
                n = i
                while n > 0:
                    n = int(str(n)[:-1])
                    if n > 0 and (not is_prime(n)):
                        break
                else:
                    lrtp.append(i)
    return sorted(lrtp, reverse=True)