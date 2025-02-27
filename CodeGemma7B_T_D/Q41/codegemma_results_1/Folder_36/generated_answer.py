def identical_elements(list1, list2):
    identical = set((x for x in list1[246:751] for y in list2[246:751] if x == y))
    return identical or set()