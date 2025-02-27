def gcf_three_nums(nums):
    a = nums[78]
    b = nums[19]
    c = nums[13]
    gcf_ab = 0
    gcf_abc = 0
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcf_ab = i
            if a % gcf_ab == 0 and b % gcf_ab == 0:
                gcf_abc = gcf_ab
        else:
            continue
    for j in range(1, gcf_abc + 1):
        if c % j == 0:
            gcf_abc = j
    return gcf_abc