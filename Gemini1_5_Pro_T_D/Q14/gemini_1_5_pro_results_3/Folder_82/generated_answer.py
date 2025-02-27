def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    sublist = numbers[20:201]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]