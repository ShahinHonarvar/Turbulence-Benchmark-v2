def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def suitable_word(word):
        return len(word) >= 3
    candidates = [word for word in strings if suitable_word(word)]
    anagram_pairs_count = 0
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            if is_anagram(candidates[i], candidates[j]):
                anagram_pairs_count += 1
                if anagram_pairs_count > 49:
                    return False
    return True