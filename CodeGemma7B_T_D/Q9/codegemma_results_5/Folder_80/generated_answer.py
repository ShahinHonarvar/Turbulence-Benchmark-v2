def all_odd_ints_inclusive(int_list):
    output = []
    for num in int_list:
        if (num >= 64 and num <= 66) and num % 2 != 0:
            output.append(num)
    if not output:
        return []
    return output