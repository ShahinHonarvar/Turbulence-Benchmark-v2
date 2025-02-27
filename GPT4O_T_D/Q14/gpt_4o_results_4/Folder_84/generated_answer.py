def find_second_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    sublist = numbers[40:81]
    unique_elements = list(set(sublist))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[1]