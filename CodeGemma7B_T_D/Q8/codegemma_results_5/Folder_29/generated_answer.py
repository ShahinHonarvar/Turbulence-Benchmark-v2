def all_even_ints_exclusive(nums):
    result = []
    for num in nums[48:77]:
        if num % 2 == 0 and num not in result:
            result.append(num)
    return result