def if_contains_anagrams(lst):

    def sort_str(s):
        return ''.join(sorted(s.lower()))
    anagrams = dict()
    for word in lst:
        if len(word) >= 3:
            sorted_word = sort_str(word)
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    count = 0
    for key in anagrams:
        n = anagrams[key]
        if n >= 2:
            count += n * (n - 1) // 2
        if count >= 18:
            return True
    return False