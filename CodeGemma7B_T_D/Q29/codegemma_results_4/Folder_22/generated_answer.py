def gcf_two_nums(nums):
    n1 = nums[24]
    n2 = nums[68]
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(smaller, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            gcf = i
            break
    return gcf