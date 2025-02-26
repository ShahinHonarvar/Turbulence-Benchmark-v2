def sum_ints_div_by_either_nums(numbers):
    total = sum((num for num in numbers[299:383] if num % 858 == 0 or num % 952 == 0))
    return total