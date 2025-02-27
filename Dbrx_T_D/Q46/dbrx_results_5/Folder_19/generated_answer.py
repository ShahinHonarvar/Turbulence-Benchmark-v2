def gcf_three_nums(nums):
    a = nums[40]
    b = nums[15]
    c = nums[99]
    return gcf_helper(a, b, c)

def gcf_helper(a, b, c):
    if b == 0:
        return a if a % c == 0 else gcf_helper(c, a % c, b)
    else:
        return gcf_helper(b, a % b, c)