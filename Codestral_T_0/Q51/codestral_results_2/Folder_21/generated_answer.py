def if_contains_anagrams(strings):
    anagram_count = [0] * 26
    for s in strings:
        if len(s) >= 3:
            key = 0
            for c in s.lower():
                if 'a' <= c <= 'z':
                    key |= 1 << ord(c) - ord('a')
            anagram_count[key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count)) <= 26