def if_contains_anagrams(lst):
    anagrams_count = 0
    sorted_strings = [''.join(sorted(s.casefold())) for s in lst if s.isascii() and len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagrams_count += 1
                if anagrams_count > 97:
                    return False
    return True