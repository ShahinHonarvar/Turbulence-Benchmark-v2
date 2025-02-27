def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        while num_str:
            if not is_prime(int(num_str)):
                break
            num_str = num_str[1:]
        else:
            result.append(num)
    return sorted(result)