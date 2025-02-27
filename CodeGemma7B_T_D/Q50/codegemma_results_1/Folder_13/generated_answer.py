def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in anagrams and len(word) >= 3:
            anagrams[key] += 1
            if anagrams[key] >= 144:
                return True
        else:
            anagrams[key] = 1
    return False