def sum_even_ints_inclusive(nums):
    result = sum([num for num in nums[209:557] if num % 2 == 0])
    return 0 if result == 0 else result