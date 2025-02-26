def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[1:9]) < 2:
        return None
    sublist = numbers[1:9]
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]