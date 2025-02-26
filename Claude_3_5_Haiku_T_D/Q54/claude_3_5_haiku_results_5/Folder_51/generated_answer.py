def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums_tuple):
    x = nums_tuple[54]
    result = []
    for num in range(2, x):
        current = num
        is_right_truncatable = True
        while current > 0:
            if not is_prime(current):
                is_right_truncatable = False
                break
            current //= 10
        if is_right_truncatable and current == 0:
            result.append(num)
    return sorted(result)