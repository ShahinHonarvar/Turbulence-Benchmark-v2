def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count > 147:
                return False
    return True