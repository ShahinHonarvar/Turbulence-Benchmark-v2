def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[61]
    result = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if trunc == i and len(str(trunc)) == 1:
                    result.append(i)
                    break
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:])
    result.sort()
    return result