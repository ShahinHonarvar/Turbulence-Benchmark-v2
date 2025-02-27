def find_second_largest_num(numbers):
    if len(numbers) < 87 or 43 >= len(numbers):
        return None
    sublist = numbers[43:87]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)