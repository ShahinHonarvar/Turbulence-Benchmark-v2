def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                pairs += anagrams[sorted_string]
                if pairs > 96:
                    return False
            else:
                anagrams[sorted_string] = 1
    return True