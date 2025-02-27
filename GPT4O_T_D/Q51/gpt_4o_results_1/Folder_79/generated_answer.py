def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i]) == sorted(strings[j]):
                    anagram_count += 1
                    if anagram_count > 173:
                        return False
    return True