def find_original_set(set1, set2, set3):
    if not set1.issubset(set2) or not set1.issubset(set3):
        return None
    elif not set2.issubset(set1) or not set2.issubset(set3):
        return None
    elif not set3.issubset(set1) or not set3.issubset(set2):
        return None
    return min({set1, set2, set3}, key=len)