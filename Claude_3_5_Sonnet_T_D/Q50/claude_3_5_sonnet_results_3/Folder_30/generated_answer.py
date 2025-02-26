def if_contains_anagrams(string_list):
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_count += 1
                if anagram_count >= 78:
                    return True
    return False