def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(7, 10):
        if i >= len(nums):
            break
        num = nums[i]
        if num % 2 == 0 or num % 3 == 0:
            sum += num
    return sum