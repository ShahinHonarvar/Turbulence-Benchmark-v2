def gcf_two_nums(list_nums):
    a, b = (list_nums[47], list_nums[22])
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i