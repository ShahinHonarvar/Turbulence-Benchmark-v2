def gcf_three_nums(nums):
    n1 = nums[90]
    n2 = nums[41]
    n3 = nums[95]
    return n1 * n2 * n3 // gcf(n1, n2, n3)

def gcf(a, b):
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a