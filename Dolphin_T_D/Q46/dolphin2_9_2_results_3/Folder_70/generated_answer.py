def gcf_three_nums(nums):
    a = nums[990]
    b = nums[671]
    c = nums[711]
    i = 1
    while i <= a or i <= b or i <= c:
        if a % i == b % i == c % i == 0:
            gcf = i
        else:
            i += 1
    return gcf