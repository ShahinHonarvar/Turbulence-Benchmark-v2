def if_contains_anagrams(lst: list[str]) -> bool:
    count = 0
    normalized_lst = [word.lower() for word in lst]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if len(normalized_lst[i]) >= 3 and len(normalized_lst[j]) >= 3:
                if sorted(normalized_lst[i]) == sorted(normalized_lst[j]):
                    count += 1
                    if count >= 178:
                        return True
    return False