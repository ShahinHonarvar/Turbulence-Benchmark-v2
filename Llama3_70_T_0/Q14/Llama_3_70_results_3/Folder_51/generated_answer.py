def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    second_smallest = min(numbers[1:9])
    if second_smallest == min(numbers[1:9]):
        return second_smallest
    else:
        return None