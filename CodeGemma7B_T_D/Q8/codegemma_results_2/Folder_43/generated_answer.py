def all_even_ints_exclusive(nums):
    result = []
    for num in nums[38:77]:
        if num % 2 == 0:
            result.append(num)
    return result