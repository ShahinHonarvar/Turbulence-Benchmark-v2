def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [''.join(sorted(s)).lower() for s in lst if len(s) >= 3]
    unique_anagrams = set()
    for s in lst:
        if s in unique_anagrams:
            anagram_count += 1
        else:
            unique_anagrams.add(s)
    return anagram_count >= 73