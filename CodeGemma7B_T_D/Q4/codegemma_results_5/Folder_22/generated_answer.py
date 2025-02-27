def all_pos_ints_exclusive(nums):
    output = []
    for num in nums:
        if num > 0 and 40 < num < 200:
            output.append(num)
    return output