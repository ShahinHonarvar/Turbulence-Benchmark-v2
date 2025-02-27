def find_second_smallest_num(numbers):
    numbers = sorted(numbers[661:925])
    return numbers[1] if len(numbers) > 1 else 'None'