def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    subsection = numbers[1:6]
    if len(set(subsection)) < 2:
        return None
    sorted_subsection = sorted(subsection)
    return sorted_subsection[1]