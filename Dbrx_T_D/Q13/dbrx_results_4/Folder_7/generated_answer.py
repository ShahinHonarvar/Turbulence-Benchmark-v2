def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 924 or len(numbers) < 661:
        return None
    sorted_numbers = sorted(numbers[661:925])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[-2]