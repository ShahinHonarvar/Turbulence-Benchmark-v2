def if_perfect_num(nums):

    def is_perfect(num):
        if num < 0:
            return False
        return sum((1 for i in range(1, num) if num % i == 0)) == num
    return is_perfect(nums[247]) if 247 < len(nums) else False