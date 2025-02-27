def if_contains_anagrams(str_list):
    str_list_lower = [string.lower() for string in str_list]
    arr = [0 for _ in range(26)]
    for string in str_list_lower:
        if len(string) >= 3:
            for char in string:
                arr[ord(char) - ord('a')] += 1
            for i in range(26):
                if arr[i] >= 2:
                    num_pairs = (arr[i] - 1) // 2
                    if num_pairs >= 46 and (num_pairs % 2 == 0 or arr[i] % 2 == 1):
                        return True
    return False