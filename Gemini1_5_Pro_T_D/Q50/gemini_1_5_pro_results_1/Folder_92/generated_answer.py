from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            groups[''.join(sorted(string.lower()))].append(string)
    counter = 0
    for key in groups:
        if len(groups[key]) >= 2:
            counter += 1
    if counter >= 2:
        return True
    else:
        return False