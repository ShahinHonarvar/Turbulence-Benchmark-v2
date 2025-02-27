def find_second_smallest_num(numbers):
    specified_range = numbers[6:9]
    if len(specified_range) < 2:
        return None
    second_smallest = sorted(specified_range)[1]
    return second_smallest