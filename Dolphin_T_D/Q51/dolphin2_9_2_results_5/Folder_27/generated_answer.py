def if_contains_anagrams(lst):
    count = 0
    dic = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in dic:
                dic[sorted_word] += 1
                count += 1
                if count > 113:
                    return False
            else:
                dic[sorted_word] = 1
    return True