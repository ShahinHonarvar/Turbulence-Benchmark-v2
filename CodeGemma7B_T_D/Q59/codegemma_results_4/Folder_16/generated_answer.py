def all_left_truncatable_prime(x):
    result = []
    for i in range(x):
        if is_prime(i) and (not has_zero(i)):
            left_truncatable = True
            n = int(str(i)[1:])
            while n > 1:
                if not is_prime(n):
                    left_truncatable = False
                    break
                n = int(str(n)[1:])
            if left_truncatable:
                result.append(i)
    return sorted(result)

def is_prime(i):
    if i <= 1:
        return False
    for n in range(2, int(i ** 0.5) + 1):
        if i % n == 0:
            return False
    return True

def has_zero(i):
    return str(i).find('0') != -1