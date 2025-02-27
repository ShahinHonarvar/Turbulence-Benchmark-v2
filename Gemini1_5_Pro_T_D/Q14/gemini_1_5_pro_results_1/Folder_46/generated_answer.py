def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[13:69]
    if len(set(sublist)) < 2:
        return None
    temp = sorted(sublist)
    return temp[1]