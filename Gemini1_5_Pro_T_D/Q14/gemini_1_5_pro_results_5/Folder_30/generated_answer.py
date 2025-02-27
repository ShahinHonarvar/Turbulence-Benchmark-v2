def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers[26:53]) < 2:
        return None
    sublist = numbers[26:53]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]