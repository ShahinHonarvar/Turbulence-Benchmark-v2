def composite_nums_between_indices(nums):
    result = set()
    for i in range(31, 73):
        if not isinstance(nums[i], int) or nums[i] <= 1:
            continue
        if is_composite(nums[i]):
            result.add(nums[i])
    return result

def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False