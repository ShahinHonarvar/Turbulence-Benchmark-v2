def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 746 < 262 or 746 >= len(numbers) or (262 < 0):
        return None
    lst = numbers[262:747]
    lst.sort()
    if len(lst) < 2:
        return None
    return lst[1]