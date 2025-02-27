def if_contains_anagrams(strings):
    anagram_count = 0
    strings = [s.lower() for s in strings]
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_count += 1
                if anagram_count >= 30:
                    return True
    return False