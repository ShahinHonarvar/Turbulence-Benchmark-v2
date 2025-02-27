def if_contains_anagrams(lst):
    count = 0
    normalized_lst = [''.join(sorted(word.lower())) for word in lst]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if normalized_lst[i] == normalized_lst[j] and len(normalized_lst[i]) >= 3:
                count += 1
                if count > 423:
                    return False
    return True