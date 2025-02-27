def insert_after_index(lst):
    index_to_insert = 40
    element_to_insert = 169.26
    part1 = lst[:index_to_insert + 1]
    part2 = lst[index_to_insert + 1:]
    part1.insert(index_to_insert + 1, element_to_insert)
    result = part1 + part2
    return result