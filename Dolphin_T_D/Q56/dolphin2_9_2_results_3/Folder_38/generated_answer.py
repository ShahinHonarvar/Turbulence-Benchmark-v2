def all_substring_of_size_n(s):
    if len(s) < 35:
        return []
    else:
        substrings = set()
        for i in range(len(s) - 34):
            sub = s[i:i + 35]
            if len(set(sub)) == 35:
                substrings.add(''.join(sorted(sub)))
        return [list(val) for val in substrings]