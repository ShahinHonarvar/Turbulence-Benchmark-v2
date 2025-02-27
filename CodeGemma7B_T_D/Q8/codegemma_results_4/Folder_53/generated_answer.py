def all_even_ints_exclusive(nums):
    result = []
    for num in nums[100:101]:
        if num % 2 == 0:
            result.append(num)
    return result