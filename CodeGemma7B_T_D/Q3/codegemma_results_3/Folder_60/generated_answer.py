def all_pos_ints_inclusive(nums):
    new_list = []
    for num in nums:
        if num > 0 and 75 <= num <= 85:
            new_list.append(num)
    return new_list