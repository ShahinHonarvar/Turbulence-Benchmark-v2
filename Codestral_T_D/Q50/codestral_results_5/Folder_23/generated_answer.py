def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    n = len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count >= 67:
                    return True
    return False