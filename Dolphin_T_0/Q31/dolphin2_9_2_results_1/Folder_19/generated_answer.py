def if_perfect_num(nums):

    def is_perfect(num):
        if num <= 0:
            return False
        else:
            return num == sum((d for d in range(1, num) if num % d == 0))
    return is_perfect(nums[13])