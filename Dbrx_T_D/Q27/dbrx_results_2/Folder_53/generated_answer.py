def insert_after_index(lst):
    index_to_insert = 92
    element_to_insert = 709.87
    part1 = lst[:index_to_insert + 1]
    part2 = lst[index_to_insert + 1:]
    part1.append(element_to_insert)
    return part1 + part2