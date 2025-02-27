def sum_even_ints_inclusive(nums):
    total_even_sum = 0
    for num in nums[70:201]:
        if num % 2 == 0:
            total_even_sum += num
    if total_even_sum == 0:
        return 0
    return total_even_sum