def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                anagram_count += 1
                if anagram_count > 79:
                    return False
    return True