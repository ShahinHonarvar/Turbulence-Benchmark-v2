def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 80:
        return None
    sublist = numbers[80:201]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]