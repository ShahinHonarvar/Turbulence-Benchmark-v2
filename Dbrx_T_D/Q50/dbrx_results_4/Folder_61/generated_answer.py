import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for length in range(3, len(max(string_list, key=len)) + 1):
        words_of_length = [word for word in string_list if len(word) == length]
        words_of_length.sort(key=lambda word: ''.join(sorted(word.lower())))
        grouped_words = itertools.groupby(words_of_length, key=lambda word: ''.join(sorted(word.lower())))
        for _, group in grouped_words:
            anagrams_count += len(list(group)) - 1
            if anagrams_count >= 8:
                return True
    return False