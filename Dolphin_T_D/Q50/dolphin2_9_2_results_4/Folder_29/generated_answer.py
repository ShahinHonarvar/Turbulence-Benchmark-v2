def if_contains_anagrams(word_list):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    count = 0
    seen = set()
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = sorted(word.lower())
        for other_word in seen:
            if is_anagram(sorted_word, other_word):
                count += 1
        seen.add(sorted_word)
    return count >= 35