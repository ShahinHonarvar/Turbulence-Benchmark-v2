def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if 51 < num < 76 and num % 1 == 0:
            result.append(num)
    return result