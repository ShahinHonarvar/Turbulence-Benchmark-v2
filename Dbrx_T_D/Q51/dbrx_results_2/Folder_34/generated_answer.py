import string

def if_contains_anagrams(string_list):
    anagrams = {}
    count = 0
    for word in string_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) < 3:
            continue
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
            count += 1
            if count > 401:
                return False
    return True