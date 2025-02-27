def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[6]
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while True:
                num //= 10
                if num == 0:
                    break
                if not is_prime(num):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)