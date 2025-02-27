def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                if anagrams[sorted_string] == string.lower():
                    continue
                anagrams[sorted_string].append(string.lower())
                if len(anagrams[sorted_string]) == 2:
                    count += 1
            else:
                anagrams[sorted_string] = [string.lower()]
    return count >= 22