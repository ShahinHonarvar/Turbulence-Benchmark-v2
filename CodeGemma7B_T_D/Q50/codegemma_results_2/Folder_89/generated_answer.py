def if_contains_anagrams(lst):
    seen_anagrams = set()
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen_anagrams:
            seen_anagrams.add(sorted_word)
            if len(seen_anagrams) >= 36:
                return True
        else:
            seen_anagrams.add(sorted_word)
    return False