def all_right_truncatable_prime(tup):
    result = []
    x = tup[758]
    for num in range(2, x):
        if all((not is_prime(int(str(num)[:-i])) for i in range(1, len(str(num))))):
            result.append(num)
    return sorted(result)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True