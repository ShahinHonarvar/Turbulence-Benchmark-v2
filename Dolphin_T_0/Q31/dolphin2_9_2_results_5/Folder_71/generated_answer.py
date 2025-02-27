def if_perfect_num(nums):
    if len(nums) < 79:
        return False
    else:
        num = nums[78]
        sum_divs = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divs += i
        return num == sum_divs