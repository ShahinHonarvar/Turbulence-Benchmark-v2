def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    unique_anagrams = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sort_string(strings[i]) == sort_string(strings[j]):
                    unique_anagrams.add((min(strings[i], strings[j]), max(strings[i], strings[j])))
    return len(unique_anagrams) <= 39