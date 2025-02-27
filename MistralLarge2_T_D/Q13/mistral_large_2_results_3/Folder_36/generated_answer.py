def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 751:
        return None
    sublist = numbers[246:751]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    second_largest = max(sublist)
    return second_largest