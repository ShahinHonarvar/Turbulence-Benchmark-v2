def if_perfect_num(nums):
    i = 320
    perfect_sum = 0
    for num in nums:
        if i in range(i, i + 7):
            perfect_sum += num
            break
        i += 1
    return perfect_sum == nums[i]