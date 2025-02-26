def sum_ints_div_by_either_nums(numbers):
    start = min(10, len(numbers))
    end = min(101, len(numbers))
    return sum((num for num in numbers[start:end] if num % 10 == 0 or num % 100 == 0))