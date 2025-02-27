def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        s = s.lower()
        if len(s) < 3 or not s.isalpha():
            continue
        s = ''.join(sorted(s))
        if s in anagram_count:
            anagram_count[s] += 1
        else:
            anagram_count[s] = 1
    pair_count = sum((n * (n - 1) // 2 for n in anagram_count.values()))
    return pair_count <= 188