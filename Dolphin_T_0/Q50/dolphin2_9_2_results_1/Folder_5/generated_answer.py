def if_contains_anagrams(lst):

    def create_word_dict(word):
        return ''.join(sorted(word.lower()))

    def check_anagrams(word1, word2):
        return create_word_dict(word1) == create_word_dict(word2)
    anagrams_count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if check_anagrams(lst[i], lst[j]):
                    anagrams_count += 1
                    if anagrams_count >= 21:
                        return True
    return anagrams_count >= 21