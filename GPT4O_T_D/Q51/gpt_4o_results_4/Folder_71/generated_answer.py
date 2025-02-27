def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    processed_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_count = 0
    for i in range(len(processed_strings)):
        for j in range(i + 1, len(processed_strings)):
            if processed_strings[i] == processed_strings[j]:
                anagram_count += 1
                if anagram_count > 9:
                    return False
    return anagram_count <= 9