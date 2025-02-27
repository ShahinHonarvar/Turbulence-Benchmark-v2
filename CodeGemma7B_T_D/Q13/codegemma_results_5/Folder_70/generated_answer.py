def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 30:
        return 'None'
    numbers = sorted(numbers)[28:33]
    return numbers[-2] if len(numbers) >= 2 else 'None'