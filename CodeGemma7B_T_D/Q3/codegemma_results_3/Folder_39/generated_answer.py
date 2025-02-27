def all_pos_ints_inclusive(nums):
    all_nums = []
    counter = 0
    for num in nums:
        if num > 0 and counter >= 20 and (counter <= 30):
            all_nums.append(num)
        counter += 1
    if not all_nums:
        return []
    return all_nums