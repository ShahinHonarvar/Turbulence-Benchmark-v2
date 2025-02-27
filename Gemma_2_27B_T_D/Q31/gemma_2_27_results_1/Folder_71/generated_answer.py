def if_perfect_num(nums):
    try:
        num = nums[78]
        sum_divisors = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_divisors += i + num // i
        return sum_divisors == num
    except IndexError:
        return False