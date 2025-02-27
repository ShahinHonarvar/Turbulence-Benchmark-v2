def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word not in seen_anagrams:
            seen_anagrams.add(sorted_word)
    return len(seen_anagrams) <= 96