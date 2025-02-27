def if_contains_anagrams(words):
    anagram_count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    frequency = {}
    for sorted_word in sorted_words:
        if sorted_word in frequency:
            anagram_count += frequency[sorted_word]
            frequency[sorted_word] += 1
        else:
            frequency[sorted_word] = 1
        if anagram_count >= 136:
            return True
    return False