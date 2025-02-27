def gcf_three_nums(nums):
    list_indices = [91, 45, 48]
    gcf = nums[list_indices[0]]
    for index in list_indices[1:]:
        gcf = gcd(gcf, nums[index])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a