def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list.sort(key=len)
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams and len(word) >= 3 and (len(anagrams[sorted_word]) + 1 <= 55):
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return len(anagrams) <= 55