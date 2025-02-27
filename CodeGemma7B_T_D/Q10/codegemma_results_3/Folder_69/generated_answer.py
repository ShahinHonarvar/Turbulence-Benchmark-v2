def all_odd_ints_exclusive(lst):
    output = []
    for num in range(68, 99):
        if num % 2 != 0:
            output.append(num)
    if output == []:
        return []
    return output