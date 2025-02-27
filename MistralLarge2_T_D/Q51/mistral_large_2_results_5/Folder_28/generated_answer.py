def if_contains_anagrams(strings):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                pairs += 1
                if pairs > 78:
                    return False
    return True