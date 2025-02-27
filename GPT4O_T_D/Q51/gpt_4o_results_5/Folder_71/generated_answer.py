def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    checked = set()
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted_string(lst[i]) == sorted_string(lst[j]):
                    pair = tuple(sorted((lst[i].lower(), lst[j].lower())))
                    if pair not in checked:
                        checked.add(pair)
                        anagram_pairs += 1
                        if anagram_pairs > 9:
                            return False
    return True