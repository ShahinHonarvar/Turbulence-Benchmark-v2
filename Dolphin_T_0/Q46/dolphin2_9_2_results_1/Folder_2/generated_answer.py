def gcf(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        return gcf(a, b % a)
    return gcf(b, a % b)

def gcf_three_nums(nums):
    return gcf(gcf(nums[307], nums[920]), nums[463])