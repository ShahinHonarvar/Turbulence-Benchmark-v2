def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    valid_anagrams = []
    strings = [s for s in strings if len(s) >= 3]
    sorted_strings = {s: sorted_lower(s) for s in strings}
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted_strings[strings[i]] == sorted_strings[strings[j]]:
                valid_anagrams.append((strings[i], strings[j]))
                if len(valid_anagrams) > 28:
                    return False
    return True