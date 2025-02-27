from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(lambda: [])
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += int(len(anagrams[key]) * (len(anagrams[key]) - 1) / 2)
    if count >= 140:
        return True
    else:
        return False