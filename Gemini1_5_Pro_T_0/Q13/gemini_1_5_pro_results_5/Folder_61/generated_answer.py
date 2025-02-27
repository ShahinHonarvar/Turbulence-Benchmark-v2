def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    else:
        sublist = numbers[:8]
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2]