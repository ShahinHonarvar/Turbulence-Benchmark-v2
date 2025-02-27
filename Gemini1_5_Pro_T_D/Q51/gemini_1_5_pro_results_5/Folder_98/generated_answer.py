def if_contains_anagrams(strings):
    strings = [string.lower() for string in strings]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted(strings[i]) == sorted(strings[j])):
                if strings.count(strings[i]) + strings.count(strings[j]) - 2 > 46:
                    return False
    return True