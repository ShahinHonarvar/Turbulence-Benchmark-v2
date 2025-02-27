def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_strs = [''.join(sorted(s.casefold())) for s in lst if len(s) >= 3]
    for i in range(len(sorted_strs)):
        for j in range(i + 1, len(sorted_strs)):
            if sorted_strs[i] == sorted_strs[j]:
                anagram_count += 1
    return anagram_count >= 77