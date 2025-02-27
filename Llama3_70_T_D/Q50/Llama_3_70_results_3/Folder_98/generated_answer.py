def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_strings = [''.join(sorted(string.lower())) for string in lst if len(string) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_count += 1
                if anagram_count >= 7:
                    return True
    return False