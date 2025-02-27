def if_contains_anagrams(strings):
    anagram_count = [0] * 26
    for s in strings:
        if len(s) < 3:
            continue
        s = s.lower()
        hash_val = 0
        for c in s:
            if 'a' <= c <= 'z':
                hash_val |= 1 << ord(c) - ord('a')
        anagram_count[hash_val] += 1
    return max(anagram_count) <= 2