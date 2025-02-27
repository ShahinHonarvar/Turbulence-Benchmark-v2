def if_contains_anagrams(words):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]) and len(words[i]) >= 3 and (len(words[j]) >= 3):
                pairs += 1
                if pairs >= 153:
                    return True
    return False