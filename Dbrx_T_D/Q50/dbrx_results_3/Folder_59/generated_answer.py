import string

def if_contains_anagrams(strings_list):
    anagrams = {}
    for word in strings_list:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    total_anagrams = sum((len(words) // 2 for words in anagrams.values()))
    return total_anagrams >= 10