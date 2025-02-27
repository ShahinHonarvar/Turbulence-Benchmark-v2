def find_second_smallest_num(numbers):
    if 50 <= len(numbers) <= 200:
        numbers = numbers[50:201]
        min_value = min(numbers)
        numbers.remove(min_value)
        if numbers:
            return min(numbers)
    return None