def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(lst):
    nums = [lst[56], lst[88], lst[51]]
    result = nums[0]
    for num in nums:
        result = gcf(result, num)
    return result