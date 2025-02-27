def if_contains_anagrams(strings):
    anagram_count = 0
    checked_pairs = set()
    for i, word1 in enumerate(strings):
        if len(word1) < 3:
            continue
        word1_sorted = ''.join(sorted(word1.lower()))
        for j, word2 in enumerate(strings[i + 1:], start=i + 1):
            if len(word2) < 3:
                continue
            word2_sorted = ''.join(sorted(word2.lower()))
            if word1_sorted == word2_sorted and (i, j) not in checked_pairs:
                anagram_count += 1
                checked_pairs.add((i, j))
                if anagram_count > 28:
                    return False
    return True