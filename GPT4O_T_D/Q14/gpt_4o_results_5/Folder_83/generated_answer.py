def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers[90:201]) < 2:
        return None
    sublist = numbers[90:201]
    first_min = min(sublist)
    sublist.remove(first_min)
    second_min = min(sublist)
    return second_min