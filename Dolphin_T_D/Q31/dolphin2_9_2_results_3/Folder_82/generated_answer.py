def if_perfect_num(nums):
    if len(nums) < 84:
        return False
    num = nums[83]
    if num <= 0:
        return False
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i != num // i:
                sum = sum + i + num // i
            else:
                sum = sum + i
    return sum == num