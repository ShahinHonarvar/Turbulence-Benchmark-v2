def gcf(nums, index1, index2, index3):
    a, b, c = (nums[index1], nums[index2], nums[index3])
    if a == 0 or b == 0 or c == 0:
        return max(a, b, c)
    else:
        while b % a != 0 or c % a != 0:
            a, b, c = (b % a, a, c % a)
        return a

def gcf_three_nums(nums):
    return gcf(nums, 16, 87, 95)