def find_second_smallest_num(numbers):
    if 62 <= len(numbers) <= 92:
        sublist = numbers[62:93]
        sublist = list(set(sublist))
        if len(sublist) > 1:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
    return None