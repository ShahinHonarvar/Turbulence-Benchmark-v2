def all_odd_ints_exclusive(num_list):
    result = []
    for num in num_list[48:74]:
        if num % 2 != 0:
            result.append(num)
    return result