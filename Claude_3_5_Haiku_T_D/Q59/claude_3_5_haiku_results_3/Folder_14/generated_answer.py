def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[78]
    result = []
    for num in range(x - 1, 1, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_left_truncatable = True
        truncated_num = num
        while len(str(truncated_num)) > 1:
            truncated_num //= 10
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)