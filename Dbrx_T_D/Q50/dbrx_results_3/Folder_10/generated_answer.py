def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                count += 1
            else:
                anagrams[sorted_string] = 1
    return count >= 52