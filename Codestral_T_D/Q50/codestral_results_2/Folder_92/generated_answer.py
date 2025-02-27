def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = [word]
            else:
                d[sorted_word].append(word)
                if len(d[sorted_word]) >= 2:
                    return True
    return False