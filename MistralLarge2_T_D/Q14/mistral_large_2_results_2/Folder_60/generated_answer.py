def find_second_smallest_num(numbers):
    if len(numbers) <= 98:
        sublist = numbers[56:99]
        if len(sublist) < 2:
            return None
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]
    return None