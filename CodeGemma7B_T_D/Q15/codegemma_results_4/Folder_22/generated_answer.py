def sum_odd_ints_inclusive(nums):
    total = 0
    count = 0
    for num in nums[40:42]:
        if num % 2 != 0:
            total += num
            count += 1
    if count == 0:
        return 0
    else:
        return total