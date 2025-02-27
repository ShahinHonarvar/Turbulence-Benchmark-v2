def gcf_two_nums(list_of_nums):
    n1 = list_of_nums[15]
    n2 = list_of_nums[99]
    while n2:
        n1, n2 = (n2, n1 % n2)
    return n1