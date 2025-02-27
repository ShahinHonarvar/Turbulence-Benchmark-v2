def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    checked = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked:
                if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                    if sorted_string(strings[i]) == sorted_string(strings[j]):
                        anagrams_count += 1
                        checked.add((i, j))
                if anagrams_count > 61:
                    return False
    return True