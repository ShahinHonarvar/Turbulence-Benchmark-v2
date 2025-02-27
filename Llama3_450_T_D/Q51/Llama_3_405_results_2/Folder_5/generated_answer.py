def if_contains_anagrams(strs):
    anagrams = {}
    count = 0
    for s in strs:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams and len(s) >= 3 and s.isalpha():
            anagrams[sorted_s] += 1
            count += 1
        elif len(s) >= 3 and s.isalpha():
            anagrams[sorted_s] = 1
    return count <= 4