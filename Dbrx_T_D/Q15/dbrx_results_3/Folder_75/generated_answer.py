def sum_odd_ints_inclusive(integer_list):
    odd_ints = []
    for i in range(56, 58):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_ints.append(integer_list[i])
    if not odd_ints:
        return 0
    else:
        return sum(odd_ints)