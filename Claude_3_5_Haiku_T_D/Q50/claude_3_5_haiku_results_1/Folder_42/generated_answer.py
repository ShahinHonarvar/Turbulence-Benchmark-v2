def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    valid_anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and are_anagrams(strings[i], strings[j]):
                valid_anagram_pairs += 1
                if valid_anagram_pairs >= 233:
                    return True
    return False