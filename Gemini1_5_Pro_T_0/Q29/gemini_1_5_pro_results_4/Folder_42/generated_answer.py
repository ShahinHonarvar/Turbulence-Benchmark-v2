def gcf_two_nums(list_of_nums):
    i = list_of_nums[90]
    j = list_of_nums[84]
    while j:
        i, j = (j, i % j)
    return i