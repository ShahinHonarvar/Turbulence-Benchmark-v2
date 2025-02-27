def if_perfect_num(nums):
    for num in nums:
        i = 1
        sum = 0
        while i < num:
            if num % i == 0:
                sum += i
            i += 1
        if num == sum:
            return True
    return False