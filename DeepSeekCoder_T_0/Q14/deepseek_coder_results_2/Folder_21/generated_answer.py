def find_second_smallest_num(numbers):
    if len(numbers) < 925 or len(numbers) < 662:
        return None
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None