def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[98]
    result = []
    for i in range(2, x):
        num_str = str(i)
        if '0' in num_str:
            continue
        is_left_truncatable = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return sorted(result)