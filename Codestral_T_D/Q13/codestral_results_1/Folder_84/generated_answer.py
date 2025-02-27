def find_second_largest_num(numbers):
    sublist = numbers[43:87]
    sublist.sort(reverse=True)
    for num in sublist:
        if num < max(sublist):
            return num
    return None