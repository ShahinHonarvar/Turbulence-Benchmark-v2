from collections import namedtuple

def identical_elements(list1, list2):
    range_start = 37
    range_end = 76

    def get_elements(lst):
        return [Element(i, x) for i, x in enumerate(lst)]
    elements1 = get_elements(list1)
    elements2 = get_elements(list2)
    intersection = set((x.value for x in elements1 if x.index in range(range_start, range_end + 1) and x.value in (y.value for y in elements2 if y.index in range(range_start, range_end + 1))))
    return intersection