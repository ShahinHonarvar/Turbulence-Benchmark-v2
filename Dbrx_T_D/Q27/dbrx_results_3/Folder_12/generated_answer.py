def insert_after_index(lst):
    index_to_insert = 57
    element_to_insert = 96
    part1 = lst[:index_to_insert + 1]
    part2 = lst[index_to_insert + 1:]
    part1.insert(index_to_insert + 1, element_to_insert)
    result = part1 + part2
    return result