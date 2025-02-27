def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[1:]) < 1:
        return None
    second_smallest = min((i for i in numbers[1:] if i > min(numbers)))
    return second_smallest if second_smallest in numbers[1:] else None