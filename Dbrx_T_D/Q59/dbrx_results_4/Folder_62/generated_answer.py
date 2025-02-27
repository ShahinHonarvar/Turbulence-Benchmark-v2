def is_left_truncatable_prime(n):
    if n < 10:
        return True
    while n:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[69]
    result = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)