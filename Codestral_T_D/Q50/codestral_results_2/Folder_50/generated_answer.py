def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lowercase_string = string.lower()
        if len(lowercase_string) >= 3:
            sorted_string = ''.join(sorted(lowercase_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lowercase_string)
            else:
                anagrams[sorted_string] = [lowercase_string]
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
            if count >= 20:
                return True
    return False