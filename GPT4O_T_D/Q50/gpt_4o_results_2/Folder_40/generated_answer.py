def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    checked = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                s1 = sorted_str(strings[i])
                s2 = sorted_str(strings[j])
                if s1 == s2 and (i, j) not in checked and ((j, i) not in checked):
                    anagram_count += 1
                    checked.add((i, j))
            if anagram_count >= 3:
                return True
    return False