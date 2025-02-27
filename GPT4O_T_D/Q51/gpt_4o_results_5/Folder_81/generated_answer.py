def if_contains_anagrams(words):

    def sorted_form(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs_count = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if sorted_form(words[i]) == sorted_form(words[j]):
                    anagram_pairs_count += 1
                    if anagram_pairs_count > 79:
                        return False
    return True