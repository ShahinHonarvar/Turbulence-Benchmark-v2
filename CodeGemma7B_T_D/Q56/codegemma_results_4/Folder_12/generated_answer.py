def all_substring_of_size_n(s):
    const = 47
    result = []
    for i in range(len(s)):
        if len(s[i:i + const]) == const:
            result.append(s[i:i + const])
    s = set(s)
    ans = []
    for i in s:
        if len(i) == const:
            ans.append(i)
    return ans