def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
            if len(anagrams[key]) > 1:
                count += 1
    return count >= 194