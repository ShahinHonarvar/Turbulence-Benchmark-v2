def find_second_largest_num(numbers):
    sublist = numbers[40:81]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]