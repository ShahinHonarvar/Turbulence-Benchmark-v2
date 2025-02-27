def sum_even_ints_inclusive(nums):
    total = 0
    for num in nums[31:73]:
        if num % 2 == 0:
            total += num
    return total if total > 0 else 0