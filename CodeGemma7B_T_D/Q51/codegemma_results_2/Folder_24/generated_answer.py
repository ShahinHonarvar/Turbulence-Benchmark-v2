def if_contains_anagrams(word_list):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    anagrams = {}
    for word in word_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    count = 0
    for word_list in anagrams.values():
        if len(word_list) > 1:
            count += len(word_list) * (len(word_list) - 1) // 2
    return count <= 96