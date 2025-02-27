def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2)
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]) and len(words[i]) >= 3:
                count += 1
                if count >= 96:
                    return True
    return False