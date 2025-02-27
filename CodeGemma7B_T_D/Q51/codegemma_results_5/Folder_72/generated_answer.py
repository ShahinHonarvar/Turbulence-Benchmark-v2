import collections

def if_contains_anagrams(str_list):
    anagram_counts = collections.defaultdict(int)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    if max(anagram_counts.values()) > 188:
        return False
    else:
        return True