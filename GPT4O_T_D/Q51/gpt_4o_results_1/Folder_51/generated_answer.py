def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    lowercased_strings = [s.lower() for s in strings]
    filtered_strings = [s for s in lowercased_strings if len(s) >= 3]
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if is_anagram(filtered_strings[i], filtered_strings[j]):
                count += 1
                if count > 116:
                    return False
    return True