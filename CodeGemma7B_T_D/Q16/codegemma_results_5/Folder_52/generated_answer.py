def sum_even_ints_inclusive(numbers):
    sum_even = 0
    for num in numbers[28:39]:
        if num % 2 == 0:
            sum_even += num
    return sum_even if sum_even else 0