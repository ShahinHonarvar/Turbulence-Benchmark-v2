def gcf_two_nums(nums_list):
    if nums_list[793] <= 0 or nums_list[449] <= 0:
        return None
    elif nums_list[793] == nums_list[449]:
        return nums_list[793]
    else:
        for i in range(min(nums_list[793], nums_list[449]), 1, -1):
            if nums_list[793] % i == 0 and nums_list[449] % i == 0:
                return i
        return 1