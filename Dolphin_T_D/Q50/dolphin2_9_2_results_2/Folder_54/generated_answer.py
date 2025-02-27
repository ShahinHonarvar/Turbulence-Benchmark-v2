def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return (sorted(str1.lower()) == sorted(str2.lower()) and len(str1), len(str2) >= 3)
    counts = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                counts += 1
                if counts >= 74:
                    return True
    return False