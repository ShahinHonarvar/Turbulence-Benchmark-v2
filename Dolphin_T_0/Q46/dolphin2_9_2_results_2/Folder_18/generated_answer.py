def gcf_three_nums(nums):
    nums = [nums[637], nums[411], nums[757]]
    gcf = nums[0]
    for num in nums[1:]:
        gcf = gcf_recursive(gcf, num)
    return gcf

def gcf_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcf_recursive(b, a % b)