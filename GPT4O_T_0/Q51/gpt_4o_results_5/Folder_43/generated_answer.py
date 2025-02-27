def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                if sorted_string(strings[i]) == sorted_string(strings[j]):
                    anagram_count += 1
                    checked_pairs.add((i, j))
                    if anagram_count > 3:
                        return False
    return True