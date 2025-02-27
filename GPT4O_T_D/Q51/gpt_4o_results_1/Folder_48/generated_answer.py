def if_contains_anagrams(lst):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    count = 0
    normalized_lst = [''.join(filter(str.isalpha, word)).lower() for word in lst]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if len(normalized_lst[i]) >= 3 and len(normalized_lst[j]) >= 3:
                if is_anagram(normalized_lst[i], normalized_lst[j]):
                    count += 1
                    if count > 277:
                        return False
    return True