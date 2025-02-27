def find_second_smallest_num(numbers):
    try:
        elements = sorted(numbers[3:6])
        return elements[1]
    except IndexError:
        return None