def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[29:94])[1]
    except IndexError:
        return None