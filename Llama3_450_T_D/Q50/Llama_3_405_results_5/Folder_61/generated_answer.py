def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for s in strings:
        s = s.lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams and len(s) >= 3:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    for key, value in anagrams.items():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count >= 8