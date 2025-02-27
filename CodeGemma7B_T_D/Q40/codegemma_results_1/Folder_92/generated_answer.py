from sortedcontainers import SortedList

def return_n_smallest_chars(characters):
    return list(OrderedDict.fromkeys(SortedList(characters, key=ord)))[:63]