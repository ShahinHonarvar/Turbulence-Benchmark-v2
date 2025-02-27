def find_second_largest_num(numbers):
    if 66 <= len(numbers) <= 93:
        numbers = numbers[66:94]
        if len(set(numbers)) > 1:
            max_number = max(numbers)
            numbers.remove(max_number)
            second_max_number = max(numbers)
            return second_max_number
    return None