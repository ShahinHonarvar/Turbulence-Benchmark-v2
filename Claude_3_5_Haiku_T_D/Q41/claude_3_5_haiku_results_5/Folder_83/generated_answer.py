def identical_elements(list1, list2):
    return set((elem for i, elem in enumerate(list1) if 90 <= i <= 200 and elem in list2[max(0, i - 90):min(len(list2), i + 111)]))