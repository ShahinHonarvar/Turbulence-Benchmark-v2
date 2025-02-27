def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
    count = 0
    for key in anagrams:
        num_anagrams = len(anagrams[key])
        count += num_anagrams * (num_anagrams - 1) // 2
        if count >= 140:
            return True
    return False