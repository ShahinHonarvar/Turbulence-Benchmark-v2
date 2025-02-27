def gcf_three_nums(nums_list):
    gcf = nums_list[36]
    for i in range(36, 86):
        gcf = gisting_common_factor(gcf, nums_list[i])
    return gcf

def gisting_common_factor(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a