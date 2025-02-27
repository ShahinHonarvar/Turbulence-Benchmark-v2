def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                count += 1
                if count >= 68:
                    return True
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    return False