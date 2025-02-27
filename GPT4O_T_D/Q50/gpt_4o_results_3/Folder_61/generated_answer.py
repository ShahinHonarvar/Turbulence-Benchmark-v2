def if_contains_anagrams(strings):
    anagram_count = 0
    n = len(strings)
    checked_pairs = set()

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in checked_pairs and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                if sorted_chars(strings[i]) == sorted_chars(strings[j]):
                    anagram_count += 1
                    if anagram_count >= 8:
                        return True
                checked_pairs.add((i, j))
    return False