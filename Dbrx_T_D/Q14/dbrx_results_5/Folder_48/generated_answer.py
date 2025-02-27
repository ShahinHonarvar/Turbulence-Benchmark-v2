def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[246:751]) < 2:
        return None
    sorted_numbers = sorted(numbers[246:751])
    second_smallest = sorted_numbers[1]
    return second_smallest