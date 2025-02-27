def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string in strings:
        if len(string) >= 3:
            for compare in strings:
                if sorted(string.lower()) == sorted(compare.lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 54