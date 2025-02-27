def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted([ch for ch in string.lower() if ch.isalpha() and len(ch) >= 3]))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return len(anagrams) <= 255