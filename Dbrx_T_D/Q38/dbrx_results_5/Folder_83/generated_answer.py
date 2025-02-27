def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 95, subsets(elements))))

def subsets(elements):
    if not elements:
        return [frozenset()]
    subs = subsets(elements[1:])
    return subs + [frozenset([elements[0]]) | s for s in subs]