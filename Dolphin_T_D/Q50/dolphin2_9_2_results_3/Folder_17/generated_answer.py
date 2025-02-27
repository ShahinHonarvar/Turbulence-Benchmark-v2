def if_contains_anagrams(words):

    def is_anagram(a, b):
        a = a.lower()
        b = b.lower()
        return sorted(a) == sorted(b)
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                count += 1
    return count >= 97