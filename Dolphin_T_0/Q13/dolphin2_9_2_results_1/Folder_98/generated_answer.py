def find_second_largest_num(numbers):
    if len(numbers) >= 7:
        numbers = numbers[0:7]
        if len(set(numbers)) >= 2:
            sorted_numbers = sorted(numbers, reverse=True)
            return sorted_numbers[1]
    return None