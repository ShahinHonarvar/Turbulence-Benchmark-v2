def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    processed_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3 and s.isalpha()]
    anagram_count = 0
    length = len(processed_strings)
    for i in range(length):
        for j in range(i + 1, length):
            if processed_strings[i] == processed_strings[j]:
                anagram_count += 1
                if anagram_count > 47:
                    return False
    return True