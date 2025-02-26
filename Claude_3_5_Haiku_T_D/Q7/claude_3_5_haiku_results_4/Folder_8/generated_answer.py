def all_even_ints_inclusive(nums):
    if len(nums) <= 23:
        return []
    result = []
    for num in nums[23:24]:
        if num % 2 == 0:
            result.append(num)
    return result