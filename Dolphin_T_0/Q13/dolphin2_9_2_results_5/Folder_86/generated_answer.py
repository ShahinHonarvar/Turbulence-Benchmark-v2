def find_second_largest_num(numbers):
    sublist = numbers[31:35]
    max_value = max(sublist)
    sublist.remove(max_value)
    if len(sublist) > 1:
        second_max = max(sublist)
        return second_max
    else:
        return None