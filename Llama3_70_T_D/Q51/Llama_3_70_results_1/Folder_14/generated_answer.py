def if_contains_anagrams(str_list):
    anagram_count = {}
    for word in str_list:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(sorted_word) < 3:
            continue
        non_english_chars = False
        for char in sorted_word:
            if ord(char) < ord('a') or ord(char) > ord('z'):
                non_english_chars = True
                break
        if non_english_chars:
            continue
        if sorted_word in anagram_count:
            anagram_count[sorted_word] += 1
        else:
            anagram_count[sorted_word] = 1
    total_anagrams = sum(anagram_count.values())
    return total_anagrams <= 474