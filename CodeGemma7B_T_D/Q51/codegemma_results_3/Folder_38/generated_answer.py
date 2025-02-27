def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        key = ''.join(sorted([c for c in word.lower() if c.isalpha() and len(c) >= 3]))
        anagrams.setdefault(key, []).append(word)
    return len(anagrams) <= 416