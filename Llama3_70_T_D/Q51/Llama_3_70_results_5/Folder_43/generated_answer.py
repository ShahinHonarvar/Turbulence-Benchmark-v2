def if_contains_anagrams(lst):
    anagrams_count = 0
    sorted_strs = [''.join(sorted(s.casefold())) for s in lst if s.isalpha() and len(s) >= 3]
    for i in range(len(sorted_strs)):
        for j in range(i + 1, len(sorted_strs)):
            if sorted_strs[i] == sorted_strs[j]:
                anagrams_count += 1
                if anagrams_count > 3:
                    return False
    return True