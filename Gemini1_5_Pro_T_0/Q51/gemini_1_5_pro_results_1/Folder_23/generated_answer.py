import itertools

def if_contains_anagrams(list_of_strings):
    pairs = itertools.combinations(list_of_strings, 2)
    count = 0
    for pair in pairs:
        str1 = pair[0].lower()
        str2 = pair[1].lower()
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
            count += 1
    return count <= 49