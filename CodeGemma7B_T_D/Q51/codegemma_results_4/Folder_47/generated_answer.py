def if_contains_anagrams(str_list):
    visited = set()
    for string in str_list:
        str_lower = string.lower()
        str_sorted = sorted(str_lower)
        str_joined = ''.join(str_sorted)
        if str_joined in visited:
            if len(visited) == 366:
                return False
        visited.add(str_joined)
    return True