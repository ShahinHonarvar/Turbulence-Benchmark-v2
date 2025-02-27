def if_contains_anagrams(str_list):
    seen = set()
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen:
            return False
        seen.add(sorted_word)
    return True