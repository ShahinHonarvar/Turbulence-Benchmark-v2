def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_and_right(n):
    while n > 10 and n % 10 > 0 and is_prime(n) and is_prime(int(str(n)[:-1])):
        n = int(str(n)[:-1])
    return n

def all_left_right_truncatable_prime(r):
    x = r[88]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and truncate_left_and_right(i) == i:
            result.append(i)
    return sorted(result)