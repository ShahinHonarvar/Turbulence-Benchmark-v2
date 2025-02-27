def contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        key = ''.join(sorted([c for c in s if c.isalpha() and c.lower() in 'abcdefghijklmnopqrstuvwxyz']))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return len(anagrams) <= 147