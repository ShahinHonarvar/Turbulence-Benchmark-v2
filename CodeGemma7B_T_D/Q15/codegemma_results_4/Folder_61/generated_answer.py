def sum_odd_ints_inclusive(nums):
    acc = 0
    for num in nums[0:8]:
        if num % 2 != 0:
            acc += num
    return acc