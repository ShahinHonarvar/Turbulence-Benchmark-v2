def if_perfect_num(nums):

    def is_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if len(nums) > 77 and nums[77] > 0:
        return is_perfect(nums[77])
    else:
        return False