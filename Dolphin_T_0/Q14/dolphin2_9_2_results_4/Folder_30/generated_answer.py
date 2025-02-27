def find_second_smallest_num(numbers):
    if 52 >= len(numbers) >= 26:
        sub_numbers = numbers[26:53]
        sub_numbers.sort()
        return sub_numbers[1] if len(sub_numbers) > 1 else None
    else:
        return None