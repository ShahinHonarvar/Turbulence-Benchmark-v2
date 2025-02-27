def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 14 or len(numbers) - 75 < 14:
        return None
    sorted_numbers = sorted(numbers[75:89])
    second_smallest = sorted_numbers[1]
    return second_smallest