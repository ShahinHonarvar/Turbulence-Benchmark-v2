def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        key_word = ''.join(sorted(word.lower()))
        if len(key_word) >= 3 and key_word not in anagrams:
            anagrams[key_word] = [word]
        elif len(key_word) >= 3:
            anagrams[key_word].append(word)
            count += 1
    return count <= 75