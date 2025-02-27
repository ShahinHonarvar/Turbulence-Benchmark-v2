def if_perfect_num(nums):
    if len(nums) < 13:
        return False
    else:
        num = nums[13]
        div_sum = 0
        for i in range(1, num):
            if num % i == 0:
                div_sum += i
        if div_sum == num:
            return True
        else:
            return False