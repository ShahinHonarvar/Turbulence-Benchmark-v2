from itertools import islice

def all_substring_of_size_n(string):
    if len(string) < 75:
        return []
    list_of_sublists = []
    for i in range(len(string) - 74):
        list_of_sublists.append(list(islice(string, i, i + 75)))
    return list({tuple(sublist) for sublist in list_of_sublists})