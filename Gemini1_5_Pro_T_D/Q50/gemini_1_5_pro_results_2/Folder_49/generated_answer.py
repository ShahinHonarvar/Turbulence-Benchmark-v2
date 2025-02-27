from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagrams[''.join(sorted(string.lower()))].append(string.lower())
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) / 2
    if count >= 59:
        return True
    else:
        return False