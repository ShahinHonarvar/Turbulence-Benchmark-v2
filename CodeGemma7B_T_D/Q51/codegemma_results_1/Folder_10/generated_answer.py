def if_contains_anagrams(lst):
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen or len(seen) >= 21:
            return False
        seen.add(sorted_word)
    return True