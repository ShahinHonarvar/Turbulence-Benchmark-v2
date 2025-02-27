def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    required_numbers = numbers[59:98]
    if len(required_numbers) < 2:
        return None
    required_numbers.sort(reverse=True)
    return required_numbers[1]