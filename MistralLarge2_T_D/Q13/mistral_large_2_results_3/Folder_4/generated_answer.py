def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = numbers[12:93]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    second_largest = max(sublist)
    return second_largest