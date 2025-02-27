def if_contains_anagrams(strings):
    lowercased_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = 0
    for i in range(len(lowercased_strings)):
        for j in range(i + 1, len(lowercased_strings)):
            if lowercased_strings[i] == lowercased_strings[j]:
                anagram_count += 1
                if anagram_count > 255:
                    return False
    return True