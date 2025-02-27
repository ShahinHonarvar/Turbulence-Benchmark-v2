def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_s.isalpha():
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 9