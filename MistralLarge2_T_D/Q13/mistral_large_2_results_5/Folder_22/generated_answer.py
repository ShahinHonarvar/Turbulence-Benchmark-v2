def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[40:201]
    if len(sublist) < 2:
        return None
    first_max = max(sublist)
    sublist.remove(first_max)
    second_max = max(sublist)
    return second_max