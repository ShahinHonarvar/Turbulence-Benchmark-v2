def if_contains_anagrams(lst):
    count = 0
    anagrams_found = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams_found:
                count += 1
                anagrams_found.remove(sorted_word)
            else:
                anagrams_found.add(sorted_word)
    return count >= 98