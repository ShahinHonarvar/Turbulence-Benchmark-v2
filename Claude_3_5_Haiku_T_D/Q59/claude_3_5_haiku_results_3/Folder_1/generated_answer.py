def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[20]
    result = []
    for num in range(x - 1, 1, -1):
        if str(num).find('0') == -1:
            is_truncatable = True
            current = num
            while current > 0:
                if not is_prime(current):
                    is_truncatable = False
                    break
                current //= 10
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)