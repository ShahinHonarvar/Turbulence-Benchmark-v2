def sum_even_ints_inclusive(nums):
    if len(nums) <= 556:
        return 0
    even_sum = 0
    for num in nums[209:557]:
        if num % 2 == 0:
            even_sum += num
    return even_sum