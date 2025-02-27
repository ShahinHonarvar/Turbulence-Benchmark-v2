def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[:8]
    max_num = max(sublist)
    sublist.remove(max_num)
    if sublist:
        return max(sublist)
    return None