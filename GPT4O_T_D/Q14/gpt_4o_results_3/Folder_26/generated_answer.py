def find_second_smallest_num(numbers):
    sublist = numbers[62:79]
    if len(sublist) < 2:
        return None
    sorted_unique_sublist = sorted(set(sublist))
    return sorted_unique_sublist[1] if len(sorted_unique_sublist) > 1 else None