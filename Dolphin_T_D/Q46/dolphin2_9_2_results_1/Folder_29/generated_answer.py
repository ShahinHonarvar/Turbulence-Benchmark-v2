def gcf(a, b, c):
    if a == 0:
        return b + c
    if b == 0:
        return a + c
    if c == 0:
        return a + b
    if a == b or a == c or b == c:
        return max(a, b, c)
    if a > b:
        if a > c:
            return gcf(a % b, b, c)
    else:
        return gcf(a, b % a, c)

def gcf_three_nums(nums):
    return gcf(nums[22], nums[97], nums[64])