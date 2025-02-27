def find_original_set(*sets):
    original_set = set().union(*sets)
    for element in original_set.copy():
        original_set.remove(element)
        if all((element not in original_set for s in sets)):
            continue
        else:
            original_set.add(element)
    return original_set