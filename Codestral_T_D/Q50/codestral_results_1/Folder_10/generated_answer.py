def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    for key in anagrams:
        anagrams_count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if anagrams_count >= 52:
            return True
    return False