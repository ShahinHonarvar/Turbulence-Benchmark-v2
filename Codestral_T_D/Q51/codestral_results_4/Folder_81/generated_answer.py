def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                count += 1
                if count > 79:
                    return False
            else:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
    return True