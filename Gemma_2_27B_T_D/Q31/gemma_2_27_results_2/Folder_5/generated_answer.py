def if_perfect_num(nums):
    if len(nums) > 67:
        total = 1
        num = nums[67]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i + num // i
        return total == num
    else:
        return False