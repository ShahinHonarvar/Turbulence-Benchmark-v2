def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_number(num):
    str_num = str(num)
    truncations = set()
    for i in range(1, len(str_num)):
        if '0' in (str_num[i:], str_num[:i]):
            return set()
        truncations.add(int(str_num[i:]))
        truncations.add(int(str_num[:i]))
    return truncations

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    for trunc in truncate_number(num):
        if not is_prime(trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    results = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            results.append(num)
    return results