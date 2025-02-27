def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s))
    words = [w.lower() for w in words if len(w) >= 3]
    sorted_words = [sort_string(w) for w in words]
    anagram_dict = {}
    pair_count = 0
    for word in sorted_words:
        if word in anagram_dict:
            pair_count += anagram_dict[word]
            anagram_dict[word] += 1
        else:
            anagram_dict[word] = 1
    return pair_count <= 22