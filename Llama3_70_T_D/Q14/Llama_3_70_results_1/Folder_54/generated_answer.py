def find_second_smallest_num(numbers):
    elements = numbers[68:87]
    if len(elements) < 2:
        return None
    elements.sort()
    return elements[1]