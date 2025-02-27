def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list.sort(key=len)
    anagrams = {}
    count = 0
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = word
        elif word != anagrams[sorted_word]:
            count += 1
    return count >= 94