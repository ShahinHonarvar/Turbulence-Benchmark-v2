def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            s = sorted_str(word)
            if s in anagram_dict:
                anagram_dict[s] += 1
            else:
                anagram_dict[s] = 1
    count = 0
    for num in anagram_dict.values():
        if num > 1:
            count += num * (num - 1) // 2
            if count >= 74:
                return True
    return False