import collections

def if_contains_anagrams(string_list):
    if len(string_list) < 68:
        return True
    string_list = [string.lower() for string in string_list]
    string_list = [''.join(sorted(s)) for s in string_list]
    string_counts = collections.Counter(string_list)
    anagram_pairs = []
    for count in string_counts.values():
        anagram_pairs.extend([(count, i) for i in range(count)])
    return sum((pair[0] for pair in anagram_pairs)) <= 68