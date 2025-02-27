def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    words = [word.lower() for word in strings if len(word) >= 3]
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                count += 1
                if count > 85:
                    return False
    return True