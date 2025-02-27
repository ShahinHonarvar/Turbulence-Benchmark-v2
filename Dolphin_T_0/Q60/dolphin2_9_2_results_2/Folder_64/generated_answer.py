def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(lst):
    x = lst[4]
    result = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str or not is_prime(num):
            continue
        while len(num_str) > 2:
            if not is_prime(int(num_str[1:-1])):
                break
            num_str = num_str[1:-1]
        if len(num_str) == 2 and is_prime(int(num_str)):
            result.append(num)
    result.sort()
    return result