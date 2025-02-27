def insert_after_index(lst):
    index_to_insert = 87
    value_to_insert = 637.22
    part1 = lst[:index_to_insert + 1]
    part2 = lst[index_to_insert + 1:]
    part1.insert(index_to_insert + 1, value_to_insert)
    return part1 + part2