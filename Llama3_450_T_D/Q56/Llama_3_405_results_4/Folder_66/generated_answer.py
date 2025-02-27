from collections import defaultdict

def all_substring_of_size_n(s):
    result = set()
    char_count = defaultdict(int)
    for i in range(len(s)):
        char_count = defaultdict(int)
        for j in range(i, len(s)):
            char_count[s[j]] += 1
            if j - i + 1 == 26:
                if all((count == 1 for count in char_count.values())):
                    result.add(s[i:j + 1])
    return list(result)