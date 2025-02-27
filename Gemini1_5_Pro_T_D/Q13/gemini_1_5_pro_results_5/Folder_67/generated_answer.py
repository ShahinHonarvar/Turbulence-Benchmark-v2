def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    sublist = numbers[22:51]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)