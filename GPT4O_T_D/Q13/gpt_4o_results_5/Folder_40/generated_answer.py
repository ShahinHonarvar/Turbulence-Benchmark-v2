def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    sublist = numbers[:3]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) >= 2 else None