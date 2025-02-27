def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    else:
        sublist = numbers[35:50]
        sorted_sublist = sorted(sublist)
        if len(sorted_sublist) >= 2:
            return sorted_sublist[1]
        else:
            return None