def if_contains_anagrams(strings):
    anagram_count = 0
    checked_pairs = set()
    strings = [s.lower() for s in strings]

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                pair = tuple(sorted((strings[i], strings[j])))
                if pair not in checked_pairs and is_anagram(strings[i], strings[j]):
                    anagram_count += 1
                    checked_pairs.add(pair)
                    if anagram_count >= 5:
                        return True
    return False