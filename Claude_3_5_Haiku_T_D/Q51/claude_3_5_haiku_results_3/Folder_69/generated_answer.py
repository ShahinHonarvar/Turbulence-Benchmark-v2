def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_length(s):
        return len(s) >= 3
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_length(strings[i]) and is_valid_length(strings[j]) and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 58