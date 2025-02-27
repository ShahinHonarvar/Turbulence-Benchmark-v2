def sum_ints_div_by_either_nums(numbers):
    start, end = (38, 52)
    return sum((num for num in numbers[start:end + 1] if num % -41 == 0 or num % -47 == 0))