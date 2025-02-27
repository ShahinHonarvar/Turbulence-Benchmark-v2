def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    processed_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(processed_strings)):
        for j in range(i + 1, len(processed_strings)):
            if processed_strings[i] == processed_strings[j]:
                anagram_pairs += 1
                if anagram_pairs >= 69:
                    return True
    return False