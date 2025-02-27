def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(s) >= 3:
            if s in anagrams:
                anagrams[s].append(string)
            else:
                anagrams[s] = [string]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 9