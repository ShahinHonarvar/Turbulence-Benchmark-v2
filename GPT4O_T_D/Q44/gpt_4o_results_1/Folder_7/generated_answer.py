def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(527, 539):
        if i < len(nums) and is_composite(nums[i]):
            composite_numbers.add(nums[i])
    return composite_numbers