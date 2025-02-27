def all_right_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                result.append(i)
    return sorted(result, reverse=True)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True