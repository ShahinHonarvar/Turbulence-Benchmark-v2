def if_perfect_num(nums):

    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    if len(nums) > 19 and nums[19] > 0:
        return is_perfect(nums[19])
    else:
        return False