from collections import defaultdict

def all_substring_of_size_n(s):
    result = set()
    char_count = defaultdict(int)
    left = 0
    for right in range(len(s)):
        char_count[s[right]] += 1
        while right - left + 1 > 26:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        if right - left + 1 == 26 and len(char_count) == 26:
            result.add(s[left:right + 1])
    return list(result)