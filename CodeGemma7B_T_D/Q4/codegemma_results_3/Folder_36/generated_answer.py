def all_pos_ints_exclusive(nums):
    output = []
    for num in nums:
        if num > 0 and num not in range(599, 768):
            output.append(num)
    return output