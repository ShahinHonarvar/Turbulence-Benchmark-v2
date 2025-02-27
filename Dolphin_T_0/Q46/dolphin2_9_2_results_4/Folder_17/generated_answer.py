def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    nums = [lst[20], lst[51], lst[62]]
    gcf_val = nums[0]
    for num in nums:
        gcf_val = gcf(gcf_val, num)
    return gcf_val