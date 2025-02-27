def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        anagrams[key] = anagrams.get(key, 0) + 1
    return len(anagrams) <= 85