def sum_even_ints_inclusive(numbers):
    start_index = 4
    end_index = 4
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < 0 or i >= len(numbers):
            continue
        num = numbers[i]
        if num % 2 == 0:
            sum += num
    return sum