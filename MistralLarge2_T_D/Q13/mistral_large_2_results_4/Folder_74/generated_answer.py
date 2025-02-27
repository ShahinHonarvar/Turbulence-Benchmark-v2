def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    sublist = numbers[17:79]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    second_largest = max(sublist)
    return second_largest