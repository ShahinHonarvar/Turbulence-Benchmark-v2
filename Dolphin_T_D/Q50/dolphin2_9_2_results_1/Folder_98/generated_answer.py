def if_contains_anagrams(lst):

    def check_anagram(str1, str2):
        return sorted(str1.upper()) == sorted(str2.upper())

    def is_pair_anagram(str1, str2):
        if check_anagram(str1, str2):
            return True
        return False
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) > 2:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) > 2 and is_pair_anagram(lst[i], lst[j]):
                    count += 1
    if count >= 7:
        return True
    else:
        return False