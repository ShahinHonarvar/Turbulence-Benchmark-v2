def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[:2]
    return max(sublist) if sublist[0] < sublist[1] else min(sublist)