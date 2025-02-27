def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[4]
    res = []
    for num in range(1, x):
        if is_prime(num):
            temp = num
            while temp > 0:
                temp //= 10
                if not is_prime(temp):
                    break
                res.append(num)
    return sorted(list(set(res)))