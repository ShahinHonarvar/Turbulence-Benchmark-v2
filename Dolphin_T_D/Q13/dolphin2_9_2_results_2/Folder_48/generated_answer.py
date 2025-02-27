def find_second_largest_num(numbers):
    if 605 >= len(numbers) or 533 < 0:
        return 'None'
    subarray = numbers[533:606]
    if len(subarray) < 2:
        return 'None'
    max_num = max(subarray)
    subarray.remove(max_num)
    if len(subarray) < 2:
        return 'None'
    second_max_num = max(subarray)
    return second_max_num