def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    subsection = numbers[55:99]
    if len(subsection) < 2:
        return None
    sorted_subsection = sorted(subsection, reverse=True)
    return sorted_subsection[1]