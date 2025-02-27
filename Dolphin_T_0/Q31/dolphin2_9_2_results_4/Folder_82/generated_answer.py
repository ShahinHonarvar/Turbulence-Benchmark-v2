def if_perfect_num(nums):

    def is_perfect(num):
        if num < 1:
            return False
        else:
            sum_divisors = 0
            for i in range(1, num):
                if num % i == 0:
                    sum_divisors += i
            return sum_divisors == num
    return is_perfect(nums[83])