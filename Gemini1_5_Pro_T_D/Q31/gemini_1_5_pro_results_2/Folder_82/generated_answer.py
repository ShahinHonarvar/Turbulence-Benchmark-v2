def if_perfect_num(nums):
    if len(nums) <= 83:
        return False
    num = nums[83]
    if num <= 1:
        return False
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
    return sum == num