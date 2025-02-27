def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        sublist = numbers[56:58]
        if sublist[0] < sublist[1]:
            return sublist[1]
        else:
            return sublist[0]