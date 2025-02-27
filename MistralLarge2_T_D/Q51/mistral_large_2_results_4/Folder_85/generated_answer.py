from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = 0
    word_dict = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        count += word_dict[norm_word]
        word_dict[norm_word] += 1
    return count <= 276