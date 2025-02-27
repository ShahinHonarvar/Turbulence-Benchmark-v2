def if_contains_anagrams(strings):
    anagram_count = 0

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    filtered_strings = [s.lower() for s in strings if len(s) >= 3]
    checked_pairs = set()
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if (i, j) not in checked_pairs:
                if is_anagram(filtered_strings[i], filtered_strings[j]):
                    anagram_count += 1
                    checked_pairs.add((i, j))
                    if anagram_count > 5:
                        return False
    return True