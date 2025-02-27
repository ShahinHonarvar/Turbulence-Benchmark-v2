def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:5]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    if sorted_sublist[1] == float('inf'):
        return None
    return sorted_sublist[1]