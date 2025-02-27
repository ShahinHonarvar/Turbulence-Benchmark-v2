def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tp):
    x = tp[98]
    result = []
    for n in range(2, x):
        if is_prime(n):
            temp = n
            while temp >= 10:
                temp = int(str(temp)[:-1])
                if not is_prime(temp):
                    break
            else:
                result.append(n)
    result.sort()
    return result