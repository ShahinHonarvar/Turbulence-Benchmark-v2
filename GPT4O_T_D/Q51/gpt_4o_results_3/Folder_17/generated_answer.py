def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s))
    words = [word.lower() for word in words]
    word_map = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_string(word)
            if sorted_word in word_map:
                word_map[sorted_word] += 1
            else:
                word_map[sorted_word] = 1
    pairs_count = 0
    for count in word_map.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count <= 22