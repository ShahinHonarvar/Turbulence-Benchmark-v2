def if_contains_anagrams(strs):
    anagram_count = 0
    strs = [s.lower() for s in strs if len(s) >= 3]
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if sorted(strs[i]) == sorted(strs[j]):
                anagram_count += 1
    return anagram_count >= 60