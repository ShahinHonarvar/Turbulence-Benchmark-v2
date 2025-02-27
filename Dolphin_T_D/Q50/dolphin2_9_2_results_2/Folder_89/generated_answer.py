def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        lowercase_word = word.lower()
        if len(lowercase_word) >= 3:
            sorted_word = ''.join(sorted(lowercase_word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
                if len(anagrams[sorted_word]) == 2:
                    count += 1
    return count >= 36