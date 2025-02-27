def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                sorted_i = sorted_chars(lst[i])
                sorted_j = sorted_chars(lst[j])
                if sorted_i == sorted_j and (i, j) not in seen:
                    anagram_count += 1
                    seen.add((i, j))
                if anagram_count > 2:
                    return False
    return True