import string

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    english_letters = set(string.ascii_lowercase + string.ascii_uppercase)
    for word1 in list_of_strings:
        if len(word1) < 3:
            continue
        word1 = ''.join(sorted(word1.lower()))
        for word2 in list_of_strings:
            if word1 == word2:
                continue
            if len(word2) < 3:
                continue
            word2 = ''.join(sorted(word2.lower()))
            if set(word1) <= english_letters and set(word2) <= english_letters and (word1 == word2):
                anagrams_count += 1
                if anagrams_count > 14:
                    return False
    return True