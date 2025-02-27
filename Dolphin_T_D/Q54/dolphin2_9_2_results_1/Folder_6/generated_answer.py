def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[74]
    res = []
    for num in range(1, x):
        if is_prime(num):
            trunc = num
            while trunc and is_prime(trunc):
                trunc //= 10
                if trunc <= 1:
                    res.append(num)
    return sorted(res)