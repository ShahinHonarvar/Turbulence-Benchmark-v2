def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 88:
        return None
    max_num = max(numbers[30:88])
    numbers.remove(max_num)
    second_max_num = max(numbers[30:88])
    return second_max_num if second_max_num < max_num else None