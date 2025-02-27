def gcf(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    nums = [lst[93], lst[94], lst[57]]
    gc = nums[0]
    for num in nums[1:]:
        gc = gcf(gc, num)
    return gc