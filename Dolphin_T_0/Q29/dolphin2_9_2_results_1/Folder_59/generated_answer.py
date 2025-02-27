def gcf_two_nums(list_of_nums):
    gcf = 0
    for i in range(1, min(list_of_nums[3], list_of_nums[8]) + 1):
        if list_of_nums[3] % i == 0 and list_of_nums[8] % i == 0:
            gcf = i
    return gcf