def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagrams_count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagrams_count += 1
    return anagrams_count >= 246