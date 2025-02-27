def all_even_ints_exclusive(nums):
    result = []
    for num in nums[48:74]:
        if num % 2 == 0 and num != 50:
            result.append(num)
    return result