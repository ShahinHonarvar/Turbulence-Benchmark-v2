def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sort_string(strings[i]) == sort_string(strings[j])):
                anagrams.append((strings[i], strings[j]))
                if len(anagrams) > 43:
                    return False
    return True