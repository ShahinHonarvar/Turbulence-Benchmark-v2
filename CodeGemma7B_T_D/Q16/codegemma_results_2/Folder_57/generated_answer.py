def sum_even_ints_inclusive(nums):
    total = 0
    count = 0
    for index, num in enumerate(nums):
        if index in range(27, 56) and num % 2 == 0:
            total += num
            count += 1
    if count == 0:
        return 0
    return total