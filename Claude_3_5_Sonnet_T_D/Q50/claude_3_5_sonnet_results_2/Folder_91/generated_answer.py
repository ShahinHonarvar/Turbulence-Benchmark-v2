def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = set()
    for i in range(len(string_list)):
        word = string_list[i].lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            anagram_count += 1
            if anagram_count >= 6:
                return True
        else:
            seen.add(sorted_word)
    return False