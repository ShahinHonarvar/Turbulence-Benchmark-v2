def sum_even_ints_inclusive(nums):
    total = 0
    for num in nums[42:69]:
        if num % 2 == 0:
            total += num
    if total == 0:
        return 0
    return total