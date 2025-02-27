def all_even_ints_exclusive(nums):
    result = []
    for num in range(nums[0], nums[6]):
        if num % 2 == 0 and num != nums[6]:
            result.append(num)
    return result