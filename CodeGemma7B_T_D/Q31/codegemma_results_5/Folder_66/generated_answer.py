def if_perfect_num(nums):
    if len(nums) > 42:
        num = nums[42]
        sum = 0
        for i in range(1, int(num / 2 + 1)):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False
    else:
        return False