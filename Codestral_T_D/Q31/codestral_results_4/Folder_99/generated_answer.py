def if_perfect_num(nums):
    index = 733
    if index < len(nums):
        num = nums[index]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    return False