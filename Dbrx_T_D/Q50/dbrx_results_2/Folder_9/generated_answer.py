from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_pairs = set()
    anagram_indices_dict = defaultdict(list)
    for index, string in enumerate(strings_list):
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_indices_dict[sorted_string].append(index)
    for indices in anagram_indices_dict.values():
        if len(indices) >= 2:
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if indices[i] != indices[j]:
                        anagrams_count += 1
                        anagrams_pairs.add(frozenset([indices[i], indices[j]]))
    return (anagrams_count >= 66, anagrams_pairs)