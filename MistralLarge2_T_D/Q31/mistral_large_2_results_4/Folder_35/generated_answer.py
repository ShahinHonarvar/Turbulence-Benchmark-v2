def if_perfect_num(nums):

    def is_perfect(num):
        return num == sum((i for i in range(1, num) if num % i == 0))
    return is_perfect(nums[993]) if len(nums) > 993 else False