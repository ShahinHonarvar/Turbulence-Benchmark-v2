def if_contains_anagrams(text_list):
    seen_anagrams = set()
    for text in text_list:
        text = text.casefold()
        sorted_text = ''.join(sorted(text))
        if len(sorted_text) >= 3 and sorted_text in seen_anagrams:
            if len(seen_anagrams) <= 6:
                return True
            return False
        seen_anagrams.add(sorted_text)
    return True