def sum_even_ints_inclusive(nums):
    total_sum = 0
    for num in nums[21:98]:
        if num % 2 == 0:
            total_sum += num
    if total_sum == 0:
        return 0
    return total_sum