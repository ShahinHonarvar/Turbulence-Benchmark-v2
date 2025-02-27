def find_second_smallest_num(numbers):
    if len(numbers[1:9]) < 2:
        return None
    second_smallest = min(numbers[1:9][1:])
    if second_smallest == min(numbers[1:9]):
        return None
    return second_smallest