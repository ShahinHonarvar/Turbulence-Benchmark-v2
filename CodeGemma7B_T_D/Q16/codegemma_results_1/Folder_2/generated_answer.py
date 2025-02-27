def sum_even_ints_inclusive(nums):
    total = 0
    for num in nums[15:40]:
        if num % 2 == 0:
            total += num
    return 0 if total == 0 else total