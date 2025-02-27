def identical_elements(listA, listB):
    return set((a for a in listA for b in listB if a == b and 0 <= listA.index(a) <= 1 and (0 <= listB.index(b) <= 1)))