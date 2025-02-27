def find_second_smallest_num(numbers):
    try:
        second_smallest = min(set(numbers[56:99]) - {min(numbers[56:99])})
    except ValueError:
        second_smallest = None
    return second_smallest