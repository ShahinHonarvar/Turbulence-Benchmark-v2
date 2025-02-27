def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    else:
        sublist = numbers[28:41]
        sorted_sublist = sorted(sublist, reverse=True)
        if len(sorted_sublist) < 2 or sorted_sublist[0] == sorted_sublist[1]:
            return None
        else:
            return sorted_sublist[1]