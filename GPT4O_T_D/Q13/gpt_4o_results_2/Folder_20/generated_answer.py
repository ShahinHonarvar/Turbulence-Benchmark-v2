def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sublist = numbers[56:67]
    if len(sublist) < 2:
        return None
    unique_elements = list(set(sublist))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort(reverse=True)
    return unique_elements[1]