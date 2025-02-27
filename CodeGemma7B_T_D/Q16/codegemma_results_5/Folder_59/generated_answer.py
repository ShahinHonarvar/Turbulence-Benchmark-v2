def sum_even_ints_inclusive(nums):
    if not any((num % 2 == 0 for num in nums)):
        return 0
    sum_even = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 9 and (nums[i] % 2 == 0):
            sum_even += nums[i]
    return sum_even