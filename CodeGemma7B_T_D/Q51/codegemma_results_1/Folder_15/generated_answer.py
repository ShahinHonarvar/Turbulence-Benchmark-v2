def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen_anagrams:
            if len(seen_anagrams) >= 20:
                return False
            continue
        seen_anagrams.add(sorted_word)
    return True