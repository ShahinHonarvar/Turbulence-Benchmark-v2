def all_even_ints_inclusive(nums):
    result = []
    for num in nums[37:77]:
        if num % 2 == 0:
            result.append(num)
    return result