def find_second_largest_num(numbers):
    numbers = numbers[36:47]
    if len(numbers) < 2:
        return None
    numbers.remove(max(numbers))
    return max(numbers)