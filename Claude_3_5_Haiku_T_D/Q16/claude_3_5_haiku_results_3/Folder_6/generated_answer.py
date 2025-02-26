def sum_even_ints_inclusive(nums):
    if len(nums) <= 66:
        return 0
    even_ints_sum = 0
    for num in nums[10:67]:
        if num % 2 == 0:
            even_ints_sum += num
    return even_ints_sum