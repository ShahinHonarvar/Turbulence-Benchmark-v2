def gcf_three_nums(nums):
    a = nums[944]
    b = nums[814]
    c = nums[865]
    while c:
        a, b, c = (b, c, a % b)
    return a