def is_perfect_num(nums):
    perfect_num = nums[35]
    sum = 1
    i = 2
    while i * i <= perfect_num:
        if perfect_num % i:
            i += 1
        elif perfect_num % (i * i) != 0:
            sum = sum + i
            i += 1
        else:
            i += 1
    if perfect_num == sum:
        return True
    else:
        return False