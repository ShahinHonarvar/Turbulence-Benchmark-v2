def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_pairs_count = 0
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings if len(''.join(filter(str.isalpha, s))) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if is_anagram(normalized_strings[i], normalized_strings[j]):
                anagram_pairs_count += 1
                if anagram_pairs_count > 88:
                    return False
    return True