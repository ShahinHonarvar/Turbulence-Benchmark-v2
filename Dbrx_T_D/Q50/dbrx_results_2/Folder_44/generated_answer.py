import string

def if_contains_anagrams(string_list):
    anagrams = {}
    for word in string_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
    total_anagrams = sum([value // 2 for value in anagrams.values()])
    return total_anagrams >= 44