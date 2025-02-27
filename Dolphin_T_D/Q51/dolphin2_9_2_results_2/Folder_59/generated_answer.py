def if_contains_anagrams(lst):
    anagrams_count = 0
    seen = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in seen:
                anagrams_count += 1
                if anagrams_count > 15:
                    return True
            else:
                seen.add(sorted_word)
    return False