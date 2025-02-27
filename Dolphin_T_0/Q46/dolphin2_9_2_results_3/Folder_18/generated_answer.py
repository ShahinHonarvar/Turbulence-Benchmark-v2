def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_three_nums(nums_list):
    nums = (nums_list[637], nums_list[411], nums_list[757])
    gcf = nums[0]
    for num in nums[1:]:
        gcf = gcd(gcf, num)
    return gcf