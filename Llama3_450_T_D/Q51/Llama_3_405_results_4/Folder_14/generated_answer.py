def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams and len(s) >= 3 and s.isalpha():
            count += anagrams[sorted_str]
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    return count <= 474