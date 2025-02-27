def sum_odd_ints_inclusive(nums):
    i = 0
    sum_odd = 0
    for num in nums[91:99]:
        if num % 2 != 0:
            sum_odd += num
            i += 1
    if i == 0:
        return 0
    return sum_odd