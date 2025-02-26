def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = {}
    for word in string_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            seen[sorted_word].append(word)
        else:
            seen[sorted_word] = [word]
    for anagram_group in seen.values():
        group_size = len(anagram_group)
        if group_size > 1:
            anagram_count += group_size * (group_size - 1) // 2
        if anagram_count >= 17:
            return True
    return False