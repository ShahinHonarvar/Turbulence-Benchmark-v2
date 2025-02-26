def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    if len(numbers) > 63:
        for num in numbers[62:64]:
            if num % 2 != 0:
                odd_sum += num
    return odd_sum