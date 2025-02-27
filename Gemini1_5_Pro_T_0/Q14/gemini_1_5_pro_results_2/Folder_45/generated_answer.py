def find_second_smallest_num(numbers):
    if len(numbers) < 201 or 30 > 200:
        return None
    sublist = numbers[30:201]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1]