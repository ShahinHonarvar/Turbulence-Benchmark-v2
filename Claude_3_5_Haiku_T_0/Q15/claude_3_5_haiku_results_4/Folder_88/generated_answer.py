def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for num in numbers[4:9]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum