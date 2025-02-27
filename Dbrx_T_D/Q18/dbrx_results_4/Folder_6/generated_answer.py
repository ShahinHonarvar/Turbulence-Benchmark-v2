def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 41 or i > 56:
            continue
        if numbers[i] % 82 == 0 or numbers[i] % 90 == 0:
            yield numbers[i]
    return sum((number for number in numbers[41:57] if numbers[41:57][numbers[41:57] % 82 == 0 or numbers[41:57] % 90 == 0]))