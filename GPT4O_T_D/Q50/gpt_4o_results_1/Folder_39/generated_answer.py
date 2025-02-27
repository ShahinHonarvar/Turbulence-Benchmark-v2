def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and ((i, j) not in checked_pairs) and (sorted_str(lst[i]) == sorted_str(lst[j])):
                anagram_count += 1
                checked_pairs.add((i, j))
            if anagram_count >= 54:
                return True
    return False