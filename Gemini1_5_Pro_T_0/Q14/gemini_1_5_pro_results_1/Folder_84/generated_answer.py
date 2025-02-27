def find_second_smallest_num(numbers):
    if len(numbers) < 81 or len(numbers) < 40:
        return None
    sublist = numbers[40:81]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]