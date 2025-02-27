def find_original_set(sets):
    all_elements = set()
    for s in sets:
        all_elements |= s
    return {e for e in all_elements if all((e in s for s in sets))}