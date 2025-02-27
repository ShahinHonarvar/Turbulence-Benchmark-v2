def find_original_set(*sets):
    universe = set().union(*sets)
    unseen_sets = set(sets)
    while unseen_sets:
        for s in unseen_sets:
            if all((s.issubset(u) for u in universe)):
                unseen_sets.remove(s)
                break
        else:
            universe.add(next(iter(unseen_sets)))
    return universe