def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                sorted_i = sorted_string(strings[i])
                sorted_j = sorted_string(strings[j])
                if sorted_i == sorted_j and (i, j) not in seen:
                    anagram_count += 1
                    seen.add((i, j))
                    if anagram_count > 2:
                        return False
    return True