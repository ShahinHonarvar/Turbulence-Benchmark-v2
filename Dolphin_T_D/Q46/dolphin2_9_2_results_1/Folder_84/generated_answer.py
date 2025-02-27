def gcf_three_nums(lst):
    nums = [lst[695], lst[710], lst[914]]
    result = nums[0]
    for i in nums:
        result = gcf(result, i)
    return result

def gcf(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a