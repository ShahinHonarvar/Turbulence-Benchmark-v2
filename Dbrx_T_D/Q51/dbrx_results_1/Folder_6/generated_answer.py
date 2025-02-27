import string

def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
                if len(anagrams[sorted_word]) == 2:
                    count += 1
                    if count > 86:
                        return False
                elif len(anagrams[sorted_word]) > 2:
                    temp_list = anagrams[sorted_word]
                    if word not in (temp_list[-1], temp_list[-2]):
                        return False
    return True