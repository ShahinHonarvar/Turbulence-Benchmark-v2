def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    for key in anagrams:
        anagram_count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return anagram_count >= 18