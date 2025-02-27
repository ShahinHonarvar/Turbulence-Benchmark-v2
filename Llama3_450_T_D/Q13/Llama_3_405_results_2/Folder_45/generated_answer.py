def find_second_largest_num(numbers):
    if len(numbers) < 201 or 30 > len(numbers):
        return None
    numbers = numbers[30:201]
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1]