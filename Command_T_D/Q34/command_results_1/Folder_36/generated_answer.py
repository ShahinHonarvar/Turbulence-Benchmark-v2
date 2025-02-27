def find_original_set(S):
    universe = set()
    for s in S:
        universe |= s
    present = set()
    for s in S:
        present |= s
    original = universe & present
    return original