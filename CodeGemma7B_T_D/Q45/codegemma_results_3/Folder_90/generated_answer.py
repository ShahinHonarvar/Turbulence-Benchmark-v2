def palindromes_between_indices(s):
    result = set()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        i = 0
        idx = s.find(c)
        if idx == -1:
            continue
        for i in range(idx + 1, min(idx + 6, len(s))):
            result.add(s[idx:i + 1][::-1])
    return result