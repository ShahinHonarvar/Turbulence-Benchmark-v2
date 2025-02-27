def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers) > 101:
        return None
    sorted_numbers = sorted(numbers[63:67])
    if len(sorted_numbers) < 2:
        return None
    second_smallest = sorted_numbers[1]
    return second_smallest if second_smallest != sorted_numbers[0] else None