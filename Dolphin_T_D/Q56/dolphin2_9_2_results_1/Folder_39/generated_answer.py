def all_substring_of_size_n(s):
    if len(set(s)) < 94:
        return []
    else:
        result = set()
        for i in range(len(s)):
            for j in range(i + 94 <= len(s)):
                result.add(s[i:j])
        return list(result)