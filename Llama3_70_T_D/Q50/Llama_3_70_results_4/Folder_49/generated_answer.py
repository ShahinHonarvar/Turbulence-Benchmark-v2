def if_contains_anagrams(strings):
    anagrams_count = 0
    strings_lower = [s.lower() for s in strings]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings_lower[i]) >= 3 and len(strings_lower[j]) >= 3 and (sorted(strings_lower[i]) == sorted(strings_lower[j])):
                anagrams_count += 1
    return anagrams_count >= 59