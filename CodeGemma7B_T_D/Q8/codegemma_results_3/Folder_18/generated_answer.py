def all_even_ints_exclusive(nums):
    result = []
    for num in nums[57:84]:
        if num % 2 == 0:
            result.append(num)
    return result