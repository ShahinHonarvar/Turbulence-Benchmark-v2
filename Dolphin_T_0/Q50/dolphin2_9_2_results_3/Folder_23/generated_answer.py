def if_contains_anagrams(list_of_strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_pairs += 1
    return anagram_pairs >= 67