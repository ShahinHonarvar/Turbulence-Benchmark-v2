def if_perfect_num(nums):
    if nums[64] == perfect_num(nums[64]):
        return True
    else:
        return False

    def perfect_num(num):
        sumOfDividers = 0
        for divisor in range(1, num):
            if num % divisor == 0:
                sumOfDividers += divisor
        if sumOfDividers == num:
            return True
        else:
            return False