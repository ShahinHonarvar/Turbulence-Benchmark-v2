def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 80:
        return None
    sublist = numbers[80:201]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]