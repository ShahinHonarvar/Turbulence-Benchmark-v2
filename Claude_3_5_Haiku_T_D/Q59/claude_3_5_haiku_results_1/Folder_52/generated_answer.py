def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[52]
    result = []
    for num in range(x - 1, 1, -1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_left_truncatable = True
        for i in range(len(num_str)):
            curr_num = int(num_str[i:])
            if not is_prime(curr_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(num)
    return sorted(result, reverse=True)