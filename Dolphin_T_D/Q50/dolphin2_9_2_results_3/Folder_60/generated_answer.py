def if_contains_anagrams(lst):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    pairs = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if is_anagram(lst[i], lst[j]):
                    pairs += 1
    return pairs >= 60