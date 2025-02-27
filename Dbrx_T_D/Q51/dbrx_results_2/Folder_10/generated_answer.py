import string

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and all((c in string.ascii_letters for c in sorted_string)):
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    count = sum((value // 2 for value in anagrams.values()))
    return count <= 21