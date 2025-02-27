def if_contains_anagrams(lst: list[str]) -> bool:
    count = 0
    normalized_list = [word.lower() for word in lst]
    for i in range(len(normalized_list)):
        for j in range(i + 1, len(normalized_list)):
            if len(normalized_list[i]) >= 3 and len(normalized_list[j]) >= 3:
                if sorted(normalized_list[i]) == sorted(normalized_list[j]):
                    count += 1
                    if count > 6:
                        return False
    return True