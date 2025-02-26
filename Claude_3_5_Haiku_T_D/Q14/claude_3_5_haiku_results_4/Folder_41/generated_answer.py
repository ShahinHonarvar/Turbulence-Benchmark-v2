def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:5]
    if not sublist:
        return None
    return sublist[0]