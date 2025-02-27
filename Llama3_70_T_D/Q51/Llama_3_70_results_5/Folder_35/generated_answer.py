def if_contains_anagrams(words):
    words = [''.join(filter(str.isalpha, word)).lower() for word in words if len(''.join(filter(str.isalpha, word))) >= 3]
    anagrams = {}
    count = 0
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            count += anagrams[sorted_word]
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return count <= 210