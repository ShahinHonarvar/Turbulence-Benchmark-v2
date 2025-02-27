def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        sublist = numbers[4:9]
        if len(set(sublist)) < 2:
            return None
        else:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]