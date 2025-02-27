def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in anagrams and key not in ['', ' ']:
            if len(anagrams[key]) >= 3:
                anagrams[key] += [word] if word not in anagrams[key] else anagrams[key]
            else:
                anagrams[key] = [word]
        else:
            anagrams[key] = [word]
    return len(filter(lambda v: len(v) >= 3, anagrams.values())) <= 68