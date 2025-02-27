import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    total_pairs = 0
    for word in list_of_strings:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
                total_pairs += 1
    return total_pairs >= 40