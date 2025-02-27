from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    word_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word)
    for key in word_dict:
        n = len(word_dict[key])
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 70:
                return True
    return anagram_count >= 70