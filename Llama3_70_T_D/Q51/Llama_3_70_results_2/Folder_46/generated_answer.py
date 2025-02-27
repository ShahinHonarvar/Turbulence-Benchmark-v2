def if_contains_anagrams(strings):
    anagrams = {}
    anagram_count = 0
    for string in strings:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) < 3:
            continue
        s = ''.join(sorted(s))
        if s in anagrams:
            anagram_count += anagrams[s]
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    return anagram_count <= 61