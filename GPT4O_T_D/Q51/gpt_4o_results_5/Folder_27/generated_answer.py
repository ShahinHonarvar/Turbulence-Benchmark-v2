def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    pair_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                pair_count += 1
                if pair_count > 113:
                    return False
    return True