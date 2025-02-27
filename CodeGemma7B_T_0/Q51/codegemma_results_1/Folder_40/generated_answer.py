def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted([char for char in string.lower() if char.isalpha() and len(char) >= 3]))
        anagrams.setdefault(key, []).append(string)
    return len(anagrams) <= 29