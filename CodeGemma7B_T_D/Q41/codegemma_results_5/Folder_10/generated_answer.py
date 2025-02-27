def identical_elements(list1, list2):
    return set((a for a, b in zip(list1, list2) if 25 <= len(list1) <= 59 and a == b))