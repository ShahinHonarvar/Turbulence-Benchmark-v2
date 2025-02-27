def gcf_two_nums(nums):
    if len(nums) < 94:
        return 'List is not long enough to have indices 59 and 93'
    else:
        num1 = nums[59]
        num2 = nums[93]
        if num1 < num2:
            small = num1
        else:
            small = num2
        for i in range(1, small + 1):
            if small % i == 0 and num1 % i == 0 and (num2 % i == 0):
                gcf = i
        return gcf