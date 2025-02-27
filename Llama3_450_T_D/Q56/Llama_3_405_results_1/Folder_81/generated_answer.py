from collections import defaultdict

def all_substring_of_size_n(s):
    n = 98
    chars = defaultdict(int)
    unique_chars = set()
    substrings = set()
    left = 0
    for right in range(len(s)):
        chars[s[right]] += 1
        unique_chars.add(s[right])
        while right - left + 1 > n:
            chars[s[left]] -= 1
            if chars[s[left]] == 0:
                unique_chars.remove(s[left])
            left += 1
        if right - left + 1 == n and len(unique_chars) == n:
            substrings.add(s[left:right + 1])
    return list(substrings)