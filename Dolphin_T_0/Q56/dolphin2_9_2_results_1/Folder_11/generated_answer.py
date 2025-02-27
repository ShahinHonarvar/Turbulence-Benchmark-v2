def all_substring_of_size_n(s):
    if len(set(s)) * 78 > len(s):
        return []
    else:
        result = [s[i:i + 78] for i in range(len(s) - 77)]
        result = list(set(result))
        for i in range(len(result)):
            if len(set(result[i])) != 78:
                result.pop(i)
        return result