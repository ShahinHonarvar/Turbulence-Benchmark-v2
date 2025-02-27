def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    gcf_ac = 0
    gcf_bc = 0
    gcf_abc = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcf_ac = i
    for i in range(1, min(b, c) + 1):
        if b % i == 0 and c % i == 0:
            gcf_bc = i
    for i in range(1, min(a, c) + 1):
        if a % i == 0 and c % i == 0:
            gcf_abc = i
    return gcf_abc