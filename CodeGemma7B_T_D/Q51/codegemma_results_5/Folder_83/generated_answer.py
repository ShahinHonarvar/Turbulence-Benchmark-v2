def if_contains_anagrams(str_list):
    if len(str_list) > 26:
        return False
    str_list = [word.lower() for word in str_list]
    str_list = sorted(str_list, key=len)
    anagrams = {}
    for word in str_list:
        key = ''.join(sorted(word))
        if key not in anagrams:
            pairs = 0
            anagrams[key] = {'word': word, 'pairs': pairs}
        else:
            if anagrams[key]['pairs'] >= 19:
                return False
            anagrams[key]['pairs'] += 1
    return True