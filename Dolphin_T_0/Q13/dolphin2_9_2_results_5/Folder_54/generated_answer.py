def find_second_largest_num(numbers):
    sublist = numbers[34:56]
    uniq_sort = list(set(sublist))
    uniq_sort.sort()
    if len(uniq_sort) < 2:
        return None
    else:
        return uniq_sort[-2]