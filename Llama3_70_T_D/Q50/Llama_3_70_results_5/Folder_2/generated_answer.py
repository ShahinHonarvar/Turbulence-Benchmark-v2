def if_contains_anagrams(strings):
    strings = [s.casefold() for s in strings]
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]) and len(strings[i]) >= 3:
                anagram_count += 1
                if anagram_count >= 246:
                    return True
    return False