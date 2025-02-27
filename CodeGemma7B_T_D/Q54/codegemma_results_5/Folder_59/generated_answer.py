def all_right_truncatable_prime(tp):
    x = tp[84]
    rtps = []
    for i in range(x - 1, 10, -1):
        if str(i)[-1] in '2357':
            if is_prime(i):
                for j in range(1, len(str(i))):
                    num = int(str(i)[:-j])
                    if not is_prime(num):
                        break
                else:
                    rtps.append(i)
    return sorted(rtps, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True