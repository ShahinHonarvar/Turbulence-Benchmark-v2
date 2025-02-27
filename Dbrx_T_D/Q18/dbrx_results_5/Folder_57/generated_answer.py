def sum_ints_div_by_either_nums(numbers):
    div_numbers = [num for num in numbers[51:77] if num % -90 == 0 or num % -59 == 0]
    return sum(div_numbers) if div_numbers else 0