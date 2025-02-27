from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                count += 1
                if count > 19:
                    return False
    return True