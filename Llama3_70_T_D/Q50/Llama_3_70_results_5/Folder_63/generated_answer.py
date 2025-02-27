def if_contains_anagrams(strings):
    anagrams_count = 0
    strings = [s.lower() for s in strings]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted(strings[i]) == sorted(strings[j])):
                anagrams_count += 1
                if anagrams_count >= 89:
                    return True
    return False