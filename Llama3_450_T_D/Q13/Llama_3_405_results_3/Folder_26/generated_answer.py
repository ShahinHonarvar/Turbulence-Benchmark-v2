def find_second_largest_num(numbers):
    if len(numbers) < 63:
        return None
    sliced_numbers = numbers[62:100]
    if len(sliced_numbers) < 2:
        return None
    return sorted(set(sliced_numbers), reverse=True)[1]