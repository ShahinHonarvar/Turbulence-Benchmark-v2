def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[43:52])[1]
    except IndexError:
        return None