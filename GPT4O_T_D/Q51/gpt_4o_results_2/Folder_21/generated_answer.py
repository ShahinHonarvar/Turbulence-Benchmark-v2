def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return sorted(w1) == sorted(w2)
    words = [w.lower() for w in words if len(w) >= 3]
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                count += 1
                if count > 26:
                    return False
    return True