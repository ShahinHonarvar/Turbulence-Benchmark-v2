from collections import Counter

def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for words in anagrams.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
        if count > 91:
            return False
    return True