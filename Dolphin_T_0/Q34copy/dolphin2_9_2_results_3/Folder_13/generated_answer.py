def find_original_set(*sets):
    return min(sets, key=lambda x: sum((int(i not in x) for sets in sets for i in sets)))