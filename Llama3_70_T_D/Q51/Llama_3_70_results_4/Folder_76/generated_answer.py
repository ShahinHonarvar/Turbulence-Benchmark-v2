def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].add(string)
        else:
            anagrams[sorted_string] = {string}
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
        if count > 91:
            return False
    return True