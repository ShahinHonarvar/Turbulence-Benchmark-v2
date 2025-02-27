def gcf_two_nums(list_of_nums):
    a = list_of_nums[198]
    b = list_of_nums[212]
    while b:
        a, b = (b, a % b)
    return a