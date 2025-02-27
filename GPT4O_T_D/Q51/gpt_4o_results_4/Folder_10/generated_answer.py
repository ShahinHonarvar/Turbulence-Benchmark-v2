def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s))

    def is_anagram(s1, s2):
        return sort_string(s1) == sort_string(s2) and len(s1) >= 3
    words = [word.lower() for word in words]
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_count += 1
                if anagram_count > 21:
                    return False
    return True