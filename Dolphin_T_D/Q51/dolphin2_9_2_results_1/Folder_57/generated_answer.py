def if_contains_anagrams(strings):
    anagram_pairs = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 74