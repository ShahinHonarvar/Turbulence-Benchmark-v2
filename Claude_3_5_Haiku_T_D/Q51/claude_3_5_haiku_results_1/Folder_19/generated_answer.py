def if_contains_anagrams(strings):

    def clean_string(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (clean_string(s1) == clean_string(s2))
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 69:
                    return False
    return True