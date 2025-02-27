def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    sublist = numbers[608:610]
    if sublist[0] < sublist[1]:
        return sublist[1]
    else:
        return sublist[0]