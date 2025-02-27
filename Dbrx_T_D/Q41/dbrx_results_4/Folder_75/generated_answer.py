def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 56 or (not all((isinstance(i, (int, float)) for i in list1))) or (not all((isinstance(i, (int, float)) for i in list2))):
        return set()
    span = list1[56:58] + list2[56:58]
    return set((k for k, v in {i: span.count(i) for i in set(span)}.items() if v > 1))