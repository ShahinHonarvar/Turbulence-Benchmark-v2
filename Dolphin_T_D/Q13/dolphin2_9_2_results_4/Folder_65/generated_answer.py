def find_second_largest_num(numbers):
    sublist = numbers[56:99]
    if len(sublist) < 2:
        return None
    else:
        max_value = max(sublist)
        sublist.remove(max_value)
        return max(sublist)