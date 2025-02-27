def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        letters = sorted(word.lower())
        key = ''.join(letters)
        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
    return len(anagrams) <= 22