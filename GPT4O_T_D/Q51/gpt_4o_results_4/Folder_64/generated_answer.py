def if_contains_anagrams(strings):
    count = 0
    lowercased = [s.lower() for s in strings]
    sorted_strings = [''.join(sorted(s)) for s in lowercased if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                count += 1
                if count > 59:
                    return False
    return True