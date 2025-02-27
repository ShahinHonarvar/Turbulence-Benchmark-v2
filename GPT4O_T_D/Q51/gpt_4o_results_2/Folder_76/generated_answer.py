def if_contains_anagrams(lst):

    def sorted_representation(s):
        return ''.join(sorted(s.lower()))
    n = len(lst)
    anagram_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted_representation(lst[i]) == sorted_representation(lst[j]):
                    anagram_count += 1
                    if anagram_count > 91:
                        return False
    return True