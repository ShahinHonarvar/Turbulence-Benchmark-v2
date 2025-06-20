def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for num in range(2, x):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result, reverse=True)