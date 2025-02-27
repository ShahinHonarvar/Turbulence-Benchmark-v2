def all_left_truncatable_prime(tup):
    x = tup[126]
    results = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            results.append(num)
    return sorted(results, reverse=True)

def is_left_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True