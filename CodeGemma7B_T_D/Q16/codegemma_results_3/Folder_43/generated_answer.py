def sum_even_ints_inclusive(nums):
    sum = 0
    for idx, num in enumerate(nums):
        if idx >= 68 and idx <= 86 and (num % 2 == 0):
            sum += num
    return sum or 0