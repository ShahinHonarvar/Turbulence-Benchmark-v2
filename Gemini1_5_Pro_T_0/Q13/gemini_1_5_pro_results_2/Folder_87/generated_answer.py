def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    sublist = numbers[36:47]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)