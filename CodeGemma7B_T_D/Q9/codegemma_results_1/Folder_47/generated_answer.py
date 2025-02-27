def all_odd_ints_inclusive(nums):
    return_list = []
    for i in range(37, 77):
        if nums[i] % 2 != 0:
            return_list.append(nums[i])
    return return_list