def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        if word in seen_anagrams or len(word) < 3:
            continue
        seen_anagrams.add(word)
    return len(seen_anagrams) <= 92