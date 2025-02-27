def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[22:64]
    if len(set(sublist)) == 1:
        return None
    temp = sorted(sublist)
    return temp[1]