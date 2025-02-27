def identical_elements(listA, listB):
    listA = listA[70:201]
    listB = listB[70:201]
    return set((a for a in listA for b in listB if a == b))