def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    sublist = numbers[:10]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None