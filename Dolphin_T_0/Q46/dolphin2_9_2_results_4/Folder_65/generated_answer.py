def gcf_three_nums(nums):
    a = nums[18]
    b = nums[10]
    c = nums[76]
    gcf = a
    for i in range(2, max(a, b, c) + 1):
        while a % i == 0 and b % i == 0 and (c % i == 0):
            gcf *= i
            a //= i
            b //= i
            c //= i
    return gcf