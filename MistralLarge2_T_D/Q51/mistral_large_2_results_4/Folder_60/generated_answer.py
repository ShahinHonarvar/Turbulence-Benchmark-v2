from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagrams(s):
        if len(s) < 3:
            return 0
        count = 0
        for word in strings:
            if word != s and is_anagram(s, word):
                count += 1
        return count
    anagram_count = sum((count_anagrams(s) for s in strings)) // 2
    return anagram_count <= 77