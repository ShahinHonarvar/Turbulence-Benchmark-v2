def if_perfect_num(nums):
    sum_of_divisors = 1
    for i in range(2, int(nums[746] ** 0.5) + 1):
        if nums[746] % i == 0:
            sum_of_divisors += i
            if i != nums[746] // i:
                sum_of_divisors += nums[746] // i
    return sum_of_divisors == nums[746]