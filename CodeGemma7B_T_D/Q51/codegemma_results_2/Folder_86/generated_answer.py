def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        if word not in anagrams:
            anagrams[word] = 1
        else:
            anagrams[word] += 1
    if len(anagrams) <= 48:
        return True
    return False