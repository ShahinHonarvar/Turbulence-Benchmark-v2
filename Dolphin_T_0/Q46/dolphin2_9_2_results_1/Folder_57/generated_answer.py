def gcf_three_nums(nums):
    numbers = [nums[90], nums[41], nums[95]]
    gcf = numbers[0]
    for num in numbers[1:]:
        gcf = math.gcd(gcf, num)
    return gcf