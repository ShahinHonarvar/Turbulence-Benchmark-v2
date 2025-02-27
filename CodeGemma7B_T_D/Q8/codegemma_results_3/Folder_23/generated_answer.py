def all_even_ints_exclusive(nums):
    result = []
    for num in nums[29:53]:
        if num % 2 == 0:
            result.append(num)
    return result