def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    count = 0
    for group in anagrams.values():
        count += (group - 1) * group // 2
    return count <= 46