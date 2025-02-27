def all_even_ints_inclusive(nums):
    if 40 <= 80:
        return []
    result = []
    for num in nums[40:81]:
        if num % 2 == 0:
            result.append(num)
    return result