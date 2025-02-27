def gcf_three_nums(nums):
    result = gcf(nums[876], gcf(nums[203], nums[100]))
    return result

def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a