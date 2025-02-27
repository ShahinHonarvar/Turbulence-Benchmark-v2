def insert_after_index(lst):
    index_to_insert = 43
    element_to_insert = 37
    part1 = lst[:index_to_insert + 1]
    part2 = lst[index_to_insert + 1:]
    part1.insert(index_to_insert + 1, element_to_insert)
    return part1 + part2