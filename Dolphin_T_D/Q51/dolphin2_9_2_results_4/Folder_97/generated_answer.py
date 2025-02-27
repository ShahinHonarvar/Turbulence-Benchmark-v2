def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    counter = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                counter[lst[i]] = counter.get(lst[i], 0) + 1
    return len(counter) <= 18