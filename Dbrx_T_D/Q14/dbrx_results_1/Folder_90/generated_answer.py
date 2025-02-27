def find_second_smallest_num(numbers):
    try:
        start, end = (527, 538)
        sub_list = sorted(numbers[start:end + 1])
        second_smallest = sub_list[1]
        return second_smallest
    except (IndexError, TypeError):
        return None