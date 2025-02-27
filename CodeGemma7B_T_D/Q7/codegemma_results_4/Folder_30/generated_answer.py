def all_even_ints_inclusive(int_list):
    solution = []
    for item in int_list[55:99]:
        if item % 2 == 0:
            solution.append(item)
    if not solution:
        return []
    else:
        return solution