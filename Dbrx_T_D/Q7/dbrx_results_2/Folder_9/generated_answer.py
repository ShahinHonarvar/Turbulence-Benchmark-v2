def all_even_ints_inclusive(numbers):
    if len(numbers) <= 73:
        return []
    start_index = 73
    end_index = 73
    while start_index >= 0 and numbers[start_index] % 2 != 0:
        start_index -= 1
    while end_index < len(numbers) and numbers[end_index] % 2 != 0:
        end_index += 1
    return numbers[start_index:end_index + 1]