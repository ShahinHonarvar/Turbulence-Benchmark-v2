def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        sorted_s = ''.join(sorted(s_lower))
        if len(s_lower) >= 3 and s_lower.isalpha():
            if sorted_s in anagrams:
                count += anagrams[sorted_s]
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    return count <= 276