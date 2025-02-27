def if_perfect_num(nums):

    def is_perfect(num):
        if num < 1:
            return False
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if len(nums) > 702:
        return is_perfect(nums[702])
    else:
        return False