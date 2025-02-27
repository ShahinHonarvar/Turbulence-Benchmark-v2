def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        sublist = numbers[62:64]
        if sublist[0] < sublist[1]:
            return sublist[1]
        else:
            return sublist[0]