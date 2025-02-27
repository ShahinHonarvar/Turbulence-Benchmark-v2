import itertools

def if_contains_anagrams(list_of_strings):
    count = 0
    for str1, str2 in itertools.combinations(list_of_strings, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1.lower()) == sorted(str2.lower())):
            count += 1
    if count <= 11:
        return True
    else:
        return False