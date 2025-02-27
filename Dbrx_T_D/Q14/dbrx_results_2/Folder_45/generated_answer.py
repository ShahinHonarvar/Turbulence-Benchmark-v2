def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[30:201]) < 2:
        return None
    min_num_1 = min(numbers[30:201])
    numbers = [num for num in numbers[30:201] if num != min_num_1]
    min_num_2 = None
    if numbers:
        min_num_2 = min(numbers)
    return min_num_2