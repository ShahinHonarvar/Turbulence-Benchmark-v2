def find_original_set(set1, set2, set3):
    """Return the smallest set that includes all three given sets."""
    original_set = set()
    original_set.update(set1)
    original_set.update(set2)
    original_set.update(set3)
    return original_set