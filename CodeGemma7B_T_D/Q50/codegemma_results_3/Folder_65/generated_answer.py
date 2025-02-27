def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in seen_anagrams:
            seen_anagrams.add(sorted_word)
        else:
            seen_anagrams.add(sorted_word)
    return len(seen_anagrams) >= 94