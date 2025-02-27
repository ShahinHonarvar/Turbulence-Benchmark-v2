def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    else:
        sublist = numbers[62:64]
        sorted_sublist = sorted(sublist, reverse=True)
        if len(sorted_sublist) < 2:
            return None
        else:
            return sorted_sublist[1]