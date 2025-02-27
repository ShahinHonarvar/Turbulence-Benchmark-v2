def gcf_three_nums(nums):
    a = nums[944]
    b = nums[814]
    c = nums[865]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a