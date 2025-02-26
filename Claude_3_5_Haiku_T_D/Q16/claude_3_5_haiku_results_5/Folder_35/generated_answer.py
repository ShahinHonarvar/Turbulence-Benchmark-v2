def sum_even_ints_inclusive(nums):
    if len(nums) <= 48:
        return 0
    even_sum = 0
    for num in nums[30:49]:
        if num % 2 == 0:
            even_sum += num
    return even_sum