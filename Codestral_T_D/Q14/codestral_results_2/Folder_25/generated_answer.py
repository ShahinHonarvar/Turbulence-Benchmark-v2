def find_second_smallest_num(numbers):
    try:
        sorted_numbers = sorted(numbers[37:77])
        return sorted_numbers[1]
    except IndexError:
        return None