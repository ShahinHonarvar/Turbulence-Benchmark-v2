def sum_even_ints_inclusive(nums):
    total_sum = 0
    for num in nums[62:79]:
        if num % 2 == 0:
            total_sum += num
    return total_sum if total_sum else 0