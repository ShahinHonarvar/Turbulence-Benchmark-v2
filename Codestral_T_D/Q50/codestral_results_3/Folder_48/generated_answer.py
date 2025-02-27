def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    count = 0
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 219