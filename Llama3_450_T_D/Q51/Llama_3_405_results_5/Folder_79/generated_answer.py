def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 173