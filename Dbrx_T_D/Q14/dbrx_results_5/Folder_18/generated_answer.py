def find_second_smallest_num(numbers):
    if len(numbers[30:49]) < 2:
        return None
    else:
        first_smallest = min(numbers[30:49])
        numbers.remove(first_smallest)
        second_smallest = min(numbers[30:49])
        return second_smallest