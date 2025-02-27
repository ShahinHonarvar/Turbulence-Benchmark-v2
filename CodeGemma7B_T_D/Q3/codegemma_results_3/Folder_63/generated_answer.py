def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 22 <= nums.index(num) <= 88:
            result.append(num)
    return result