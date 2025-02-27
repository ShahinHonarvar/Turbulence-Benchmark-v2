def find_second_smallest_num(numbers):
    if 51 >= len(numbers) >= 43:
        sublist = numbers[43:52]
        sublist.sort()
        if len(set(sublist)) > 1:
            return sublist[1]
    return None