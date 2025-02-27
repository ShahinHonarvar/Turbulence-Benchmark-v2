def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
    count = 0
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if count >= 68:
            return True
    return False