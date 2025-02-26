def sum_even_ints_inclusive(nums):
    if len(nums) <= 88:
        return 0
    even_sum = 0
    for num in nums[22:89]:
        if num % 2 == 0:
            even_sum += num
    return even_sum