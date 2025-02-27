def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        sorted_chars = ''.join(sorted(s.lower())).strip(' ')
        if sorted_chars in anagrams:
            anagrams[sorted_chars] += 1
        elif len(sorted_chars) >= 3:
            anagrams[sorted_chars] = 1
    for k, v in anagrams.items():
        count += v * (v - 1) // 2
    return count <= 318