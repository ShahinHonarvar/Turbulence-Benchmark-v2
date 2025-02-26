def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    result = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)