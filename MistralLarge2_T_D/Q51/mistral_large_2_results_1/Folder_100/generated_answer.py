from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = set()
    length_filtered_strings = [s for s in strings if len(s) >= 3]
    for i in range(len(length_filtered_strings)):
        for j in range(i + 1, len(length_filtered_strings)):
            if is_anagram(length_filtered_strings[i], length_filtered_strings[j]):
                anagram_pairs.add((length_filtered_strings[i], length_filtered_strings[j]))
    return len(anagram_pairs) <= 98