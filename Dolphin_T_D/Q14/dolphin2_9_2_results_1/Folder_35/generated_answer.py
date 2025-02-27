def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    else:
        sublist = numbers[15:40]
        sorted_sublist = sorted(set(sublist))
        if len(sorted_sublist) < 2:
            return None
        else:
            return sorted_sublist[1]