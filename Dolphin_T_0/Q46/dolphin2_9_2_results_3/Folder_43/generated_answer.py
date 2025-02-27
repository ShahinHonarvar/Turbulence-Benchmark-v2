def gcf_three_nums(nums):
    n1 = nums[33]
    n2 = nums[78]
    n3 = nums[93]
    gcf = min(n1, n2, n3)
    while gcf > 1:
        if n1 % gcf == 0 and n2 % gcf == 0 and (n3 % gcf == 0):
            return gcf
        gcf -= 1
    return 1