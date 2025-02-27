def gcf_two_nums(nums):
    num1 = nums[8]
    num2 = nums[3]
    smaller = min(num1, num2)
    gcf = smaller
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
            break
    return gcf