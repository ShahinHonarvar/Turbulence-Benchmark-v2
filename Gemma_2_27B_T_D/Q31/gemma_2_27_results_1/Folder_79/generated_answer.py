def if_perfect_num(nums):
    if len(nums) > 63:
        num = nums[63]
        sum_of_divisors = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_of_divisors += i
                if i != num // i:
                    sum_of_divisors += num // i
        return sum_of_divisors == num
    else:
        return False