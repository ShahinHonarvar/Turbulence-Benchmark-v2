def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        sublist = numbers[62:64]
        if len(sublist) == 1:
            return None
        else:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]