def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    strings = [s.lower() for s in strings]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    count += 1
                    if count > 79:
                        return False
    return True