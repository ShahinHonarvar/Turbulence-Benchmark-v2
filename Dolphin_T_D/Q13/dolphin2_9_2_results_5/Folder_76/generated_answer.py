def find_second_largest_num(numbers):
    if len(numbers) < 987:
        return None
    sublist = numbers[686:988]
    if len(set(sublist)) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    return max(sublist)