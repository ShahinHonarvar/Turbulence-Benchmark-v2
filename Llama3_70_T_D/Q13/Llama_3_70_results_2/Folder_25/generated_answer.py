def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    else:
        sublist = numbers[29:94]
        distinct_sublist = sorted(set(sublist))
        if len(distinct_sublist) < 2:
            return None
        else:
            return distinct_sublist[-2]