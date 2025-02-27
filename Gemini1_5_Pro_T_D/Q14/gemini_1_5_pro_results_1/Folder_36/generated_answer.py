def find_second_smallest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 210:
        return None
    sublist = numbers[209:557]
    if len(set(sublist)) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]