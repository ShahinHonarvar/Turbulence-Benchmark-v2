def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[1:6])[1]
    except IndexError:
        return None