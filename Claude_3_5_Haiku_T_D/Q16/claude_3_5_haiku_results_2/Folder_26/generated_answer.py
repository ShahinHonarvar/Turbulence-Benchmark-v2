def sum_even_ints_inclusive(nums):
    if len(nums) <= 99:
        return 0
    even_sum = 0
    for num in nums[62:100]:
        if num % 2 == 0:
            even_sum += num
    return even_sum