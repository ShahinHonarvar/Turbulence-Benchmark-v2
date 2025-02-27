def if_contains_anagrams(words):

    def sort_chars(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(word_list):
        anagram_count = 0
        seen = {}
        for word in word_list:
            if len(word) >= 3:
                sorted_word = sort_chars(word)
                if sorted_word in seen:
                    anagram_count += seen[sorted_word]
                    seen[sorted_word] += 1
                else:
                    seen[sorted_word] = 1
                if anagram_count > 289:
                    return False
        return True
    return count_anagrams(words)