def if_contains_anagrams(lst: list[str]) -> bool:
    anagram_count = 0
    processed_words = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) < 3 or sorted_word in processed_words:
            continue
        anagram_candidates = [w for w in lst if sorted_word == ''.join(sorted(w.lower()))]
        anagram_count += len(anagram_candidates) * (len(anagram_candidates) - 1) // 2
        processed_words.update(anagram_candidates)
    return anagram_count >= 34