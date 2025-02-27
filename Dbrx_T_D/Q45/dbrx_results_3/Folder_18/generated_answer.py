def palindromes_between_indices(s):
    result = set()
    for i in range(len(s) - 1):
        for j in range(i + 2, min(i + 7, len(s))):
            pal = ''.join(sorted(s[i:j]))[::1 if s[i:j] > s[j - 1:i - 1:-1] else -1]
            if len(pal) >= 3 and pal == pal[::-1]:
                result.add(pal)
    return result