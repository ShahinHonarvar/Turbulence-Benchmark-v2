def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        letters = ''.join(filter(str.isalpha, string.lower()))
        if len(letters) < 3:
            continue
        if letters in anagrams:
            anagrams[letters].append(string)
        else:
            anagrams[letters] = [string]
    return len(anagrams) <= 276