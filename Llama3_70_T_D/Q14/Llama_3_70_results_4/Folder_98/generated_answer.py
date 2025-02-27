def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sublist = numbers[6:]
        sorted_sublist = sorted(sublist)
        if len(sorted_sublist) < 2 or sorted_sublist[0] == sorted_sublist[1]:
            return None
        else:
            return sorted_sublist[1]