def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    else:
        sublist = numbers[37:77]
        if len(set(sublist)) < 2:
            return None
        else:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]