def sum_odd_ints_inclusive(numbers):
    nums = numbers[36:47]
    total = 0
    for num in nums:
        if num % 2 != 0:
            total += num
    if total == 0:
        return 0
    else:
        return total