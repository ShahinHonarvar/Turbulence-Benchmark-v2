def if_perfect_num(nums):

    def is_perfect(num):
        return sum((factor for factor in range(1, num) if num % factor == 0)) == num
    return is_perfect(nums[96]) if len(nums) > 96 else False