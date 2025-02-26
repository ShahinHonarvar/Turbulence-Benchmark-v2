def sum_even_ints_inclusive(nums):
    if len(nums) <= 85:
        return 0
    even_sum = 0
    for num in nums[75:86]:
        if num % 2 == 0:
            even_sum += num
    return even_sum