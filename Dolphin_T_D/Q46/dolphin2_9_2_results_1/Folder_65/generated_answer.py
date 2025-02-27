def gcf_three_nums(lst):
    nums = [lst[18], lst[10], lst[76]]
    a = nums[0]
    b = nums[1]
    c = nums[2]
    while b != 0 and c != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        if a > c:
            a = a % c
        else:
            c = c % a
    gcf = a + b + c
    return gcf