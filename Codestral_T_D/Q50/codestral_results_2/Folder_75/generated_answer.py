from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        if len(string) < 3:
            continue
        string = string.lower()
        count = Counter(string)
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
        anagram_count += len(anagram_dict[sorted_string]) - 1
        if anagram_count >= 70:
            return True
    return False