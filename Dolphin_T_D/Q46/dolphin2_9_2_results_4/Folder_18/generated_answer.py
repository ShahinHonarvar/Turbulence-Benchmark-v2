def gcf_three_nums(lst):
    nums = [lst[637], lst[411], lst[757]]
    result = nums[0]
    for i in nums:
        result = gcf(result, i)
    return result

def gcf(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a