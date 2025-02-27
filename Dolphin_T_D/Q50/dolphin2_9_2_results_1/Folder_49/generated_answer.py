def if_contains_anagrams(word_list):

    def is_anagram(a, b):
        a = a.lower()
        b = b.lower()
        return sorted(a) == sorted(b)
    result = []
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3 and is_anagram(word_list[i], word_list[j]):
                result.append((word_list[i], word_list[j]))
    return len(result) >= 59