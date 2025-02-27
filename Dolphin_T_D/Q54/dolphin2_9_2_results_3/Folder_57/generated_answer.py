import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[54]
    res = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                if not is_prime(j):
                    break
                j = j // 10
                if j == 1:
                    res.append(i)
    return sorted(res, reverse=True)