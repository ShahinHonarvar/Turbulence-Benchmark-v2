def find_second_largest_num(numbers):
    if len(numbers) < 73:
        return None
    sublist = numbers[31:73]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)