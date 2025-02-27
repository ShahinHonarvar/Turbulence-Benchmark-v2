def if_contains_anagrams(str_list):
    letter_counts = {}
    anagram_count = 0
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in letter_counts:
            letter_counts[sorted_word] += 1
            anagram_count += 2
        else:
            letter_counts[sorted_word] = 1
    return anagram_count >= 189