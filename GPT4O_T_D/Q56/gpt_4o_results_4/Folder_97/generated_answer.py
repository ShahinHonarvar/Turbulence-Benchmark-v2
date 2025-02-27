def all_substring_of_size_n(s):
    result = []
    seen = set()
    for i in range(len(s) - 141):
        substring = s[i:i + 142]
        if len(set(substring)) == 142:
            if substring not in seen:
                result.append(substring)
                seen.add(substring)
    return result