def if_contains_anagrams(words):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            key = sorted_str(word)
            anagrams[key] = anagrams.get(key, 0) + 1
    for key in anagrams:
        n = anagrams[key]
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 123:
            return True
    return False