import string

def if_contains_anagrams(word_list):
    anagrams = {}
    count = 0
    for word in word_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word].append(word)
            if len(anagrams[sorted_word]) > 1:
                count += 1
                if count > 58:
                    return False
        else:
            anagrams[sorted_word] = [word]
    return True