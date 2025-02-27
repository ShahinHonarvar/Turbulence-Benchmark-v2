def find_second_smallest_num(numbers):
    if 27 <= len(numbers) <= 55:
        sublist = numbers[26:56]
        sorted_sublist = sorted(sublist)
        if len(sorted_sublist) > 1:
            return sorted_sublist[1]
    return None