from collections import defaultdict

def all_substring_of_size_n(s):
    result = set()
    char_count = defaultdict(int)
    window_start = 0
    for window_end in range(len(s)):
        char_count[s[window_end]] += 1
        if window_end >= 26 - 1:
            if len(char_count) == 26:
                result.add(s[window_start:window_end + 1])
            char_count[s[window_start]] -= 1
            if char_count[s[window_start]] == 0:
                del char_count[s[window_start]]
            window_start += 1
    return list(result)