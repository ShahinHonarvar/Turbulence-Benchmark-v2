def find_second_largest_num(numbers):
    sublist = numbers[667:775]
    if len(sublist) <= 1:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    second_largest = max(sublist, default=None)
    return second_largest