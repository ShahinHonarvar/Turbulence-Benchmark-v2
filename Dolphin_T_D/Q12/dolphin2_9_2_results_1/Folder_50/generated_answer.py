def find_smallest_num(numbers):
    sublist = numbers[43:52]
    smallest_num = sublist[0]
    for num in sublist:
        if num < smallest_num:
            smallest_num = num
    return smallest_num