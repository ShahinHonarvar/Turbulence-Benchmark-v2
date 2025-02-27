def gcf_three_nums(nums):
    a = nums[4]
    b = nums[0]
    c = nums[8]
    gcf_ab = 1
    gcf_ac = 1
    gcf_bc = 1
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcf_ab = i
    if a > c:
        smaller = c
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if a % i == 0 and c % i == 0:
            gcf_ac = i
    if b > c:
        smaller = c
    else:
        smaller = b
    for i in range(1, smaller + 1):
        if b % i == 0 and c % i == 0:
            gcf_bc = i
    return gcf_ab * gcf_ac * gcf_bc / (gcf_ab * gcf_ac + gcf_ab * gcf_bc + gcf_ac * gcf_bc - gcf_ab * gcf_ac * gcf_bc)