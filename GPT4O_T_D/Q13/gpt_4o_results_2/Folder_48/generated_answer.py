def find_second_largest_num(numbers):
    if len(numbers) < 606:
        return None
    try:
        sublist = numbers[533:606]
        first_largest = max(sublist)
        sublist.remove(first_largest)
        second_largest = max(sublist)
        return second_largest
    except ValueError:
        return None