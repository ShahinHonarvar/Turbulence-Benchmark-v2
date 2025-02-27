def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
                count += len(anagrams[sorted_word]) - 1
                if count >= 8:
                    return True
            else:
                anagrams[sorted_word] = [word]
    return False