def all_even_ints_exclusive(nums):
    result = []
    for num in nums[20:43]:
        if num % 2 == 0:
            result.append(num)
    if not result:
        result = []
    return result