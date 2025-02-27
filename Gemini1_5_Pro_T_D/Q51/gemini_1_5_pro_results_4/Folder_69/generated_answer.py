from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagrams[''.join(sorted(string.lower()))].append(string.lower())
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        if n >= 2:
            count += int(n * (n - 1) / 2)
    if count <= 58:
        return True
    else:
        return False