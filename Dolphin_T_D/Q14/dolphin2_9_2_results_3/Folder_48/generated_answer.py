def find_second_smallest_num(numbers):
    segment = numbers[246:751]
    if len(segment) < 2:
        return None
    else:
        min_num = min(segment)
        min_num_index = numbers.index(min_num)
        numbers.pop(min_num_index)
        second_min_num = min(numbers)
        return second_min_num if second_min_num >= min_num else None