def sum_odd_ints_inclusive(nums):
    sum = 0
    for num in nums[60:201]:
        if num % 2 != 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum