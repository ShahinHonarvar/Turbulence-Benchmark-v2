def find_second_smallest_num(numbers):
    if len(numbers) < 557:
        return None
    sublist = numbers[209:557]
    if len(sublist) <= 1:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    second_smallest = min(sublist)
    return second_smallest