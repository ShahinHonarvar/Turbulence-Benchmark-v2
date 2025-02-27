from collections import defaultdict

def all_substring_of_size_n(s):
    counter = defaultdict(int)
    unique_chars = set()
    unique_strs = set()
    start = 0
    min_len = 146
    for end in range(len(s)):
        counter[s[end]] += 1
        unique_chars.add(s[end])
        while len(unique_chars) < end - start + 1:
            counter[s[start]] -= 1
            if counter[s[start]] == 0:
                unique_chars.remove(s[start])
            start += 1
        if end - start + 1 == min_len:
            unique_strs.add(s[start:end + 1])
    return list(unique_strs)