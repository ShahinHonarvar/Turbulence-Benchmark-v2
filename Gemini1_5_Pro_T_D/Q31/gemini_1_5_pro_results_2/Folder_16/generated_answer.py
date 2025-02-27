def if_perfect_num(nums):
    if len(nums) <= 162:
        return False
    num = nums[162]
    if num <= 1:
        return False
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i
    return sum == num