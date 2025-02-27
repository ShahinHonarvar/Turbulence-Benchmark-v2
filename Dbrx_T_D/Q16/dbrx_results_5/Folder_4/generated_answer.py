def sum_even_ints_inclusive(numbers_list):
    if len(numbers_list) <= 92:
        return 0
    else:
        even_numbers = [num for num in numbers_list[11:93] if num % 2 == 0]
        return sum(even_numbers) if even_numbers else 0