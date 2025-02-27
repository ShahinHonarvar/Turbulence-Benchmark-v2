def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagrams:
                count += len(anagrams[sorted_string])
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    return count >= 36