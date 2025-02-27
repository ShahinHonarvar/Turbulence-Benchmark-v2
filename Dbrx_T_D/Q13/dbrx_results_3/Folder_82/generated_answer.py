def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 181:
        return None
    numbers = numbers[20:201]
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    second_largest = sorted_numbers[-2]
    return second_largest if numbers.count(second_largest) > 0 else None