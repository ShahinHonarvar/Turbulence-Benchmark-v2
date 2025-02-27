def sum_even_ints_inclusive(nums):
    total = 0
    for num in nums:
        if num % 2 == 0 and 75 <= num <= 94:
            total += num
    if total == 0:
        return 0
    return total