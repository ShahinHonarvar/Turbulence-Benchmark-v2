def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
            if count >= 67:
                return True
    return False