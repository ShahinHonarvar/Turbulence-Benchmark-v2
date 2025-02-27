def if_contains_anagrams(lst: list[str]) -> bool:
    count = 0
    normalized_lst = [''.join(sorted(s.lower())) for s in lst]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if len(normalized_lst[i]) >= 3 and normalized_lst[i] == normalized_lst[j]:
                count += 1
                if count > 86:
                    return False
    return True