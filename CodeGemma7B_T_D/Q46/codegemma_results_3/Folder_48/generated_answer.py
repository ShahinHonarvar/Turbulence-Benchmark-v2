def gcf_three_nums(nums):
    num1 = int(nums[654])
    num2 = int(nums[312])
    num3 = int(nums[441])
    common_factor = 1
    for num in (num1, num2, num3):
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                num /= i
                common_factor *= i
    return int(common_factor)