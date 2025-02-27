def find_second_largest_num(numbers):
    if 34 <= len(numbers) <= 55:
        numbers = numbers[33:56]
        if len(numbers) < 2:
            return None
        else:
            return sorted(numbers)[-2]
    else:
        return None