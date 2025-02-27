import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += 1
    return count <= 89