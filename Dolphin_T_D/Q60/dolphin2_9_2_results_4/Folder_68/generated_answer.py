def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_no_zero(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(x, 1, -1):
        str_i = str(i)
        if has_no_zero(i) and is_prime(i):
            for j in range(len(str_i) - 1, 0, -1):
                left = int(str_i[:j])
                right = int(str_i[j:])
                if i != left and i != right and is_prime(left) and is_prime(right):
                    result.append(i)
                    break
    result.sort(reverse=True)
    return result