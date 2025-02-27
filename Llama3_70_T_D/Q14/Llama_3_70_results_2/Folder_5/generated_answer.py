def find_second_smallest_num(numbers):
    second_smallest = None
    for num in sorted(numbers[3:6]):
        if second_smallest is None:
            second_smallest = num
        elif second_smallest != num:
            return second_smallest
    return None