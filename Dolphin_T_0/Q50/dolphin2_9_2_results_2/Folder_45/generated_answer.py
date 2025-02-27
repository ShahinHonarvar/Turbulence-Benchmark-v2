def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (lst[i].lower() == ''.join(sorted(lst[j].lower() or ''))):
                anagram_pairs += 1
    return anagram_pairs