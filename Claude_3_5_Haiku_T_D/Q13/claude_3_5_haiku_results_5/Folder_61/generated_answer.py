def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[:8]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = None
    for num in sublist:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest