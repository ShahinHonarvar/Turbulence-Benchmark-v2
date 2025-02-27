def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        sublist = numbers[43:52]
        sorted_sublist = sorted(sublist)
        if len(sorted_sublist) < 2:
            return None
        else:
            return sorted_sublist[1]