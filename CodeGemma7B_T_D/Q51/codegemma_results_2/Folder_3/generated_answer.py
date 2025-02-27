def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return len(anagrams) <= 66