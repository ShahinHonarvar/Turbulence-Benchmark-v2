def if_perfect_num(nums):
    index = 29
    if index < len(nums):
        num = nums[index]
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
        return sum == num
    else:
        return False