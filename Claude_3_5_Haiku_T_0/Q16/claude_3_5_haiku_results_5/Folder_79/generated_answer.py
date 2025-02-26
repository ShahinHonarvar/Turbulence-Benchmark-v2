def sum_even_ints_inclusive(nums):
    if len(nums) < 5:
        return 0
    even_sum = 0
    for num in nums[4:5]:
        if num % 2 == 0:
            even_sum += num
    return even_sum