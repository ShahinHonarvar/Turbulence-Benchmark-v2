def all_substring_of_size_n(s):
    """
    :type s: str
    :rtype: list[str]
    """

    def get_substr(l, r):
        result = []
        seen = set()
        while l < r:
            sub = s[l:r]
            if len(sub) == len(set(sub)) and sub not in seen:
                seen.add(sub)
                result.append(sub)
            l += 1
            r -= 1
        return result

    def get_all_substrings():
        result = []
        for i in range(len(s) - 119):
            result.extend(get_substr(i, i + 120))
        return result
    return list(set(get_all_substrings()))