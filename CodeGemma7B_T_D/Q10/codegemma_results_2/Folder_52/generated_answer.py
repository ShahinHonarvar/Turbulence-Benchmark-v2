def all_odd_ints_exclusive(nums):
    temp = []
    for i in range(93, 94):
        if nums[i] % 2 != 0:
            temp.append(nums[i])
    return temp