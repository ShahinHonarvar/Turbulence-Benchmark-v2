def palindromes_between_indices(s):
    chars = list(s[1:6].lower())
    result = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            if chars[i:j + 1] == chars[i:j + 1][::-1] and len(chars[i:j + 1]) >= 6:
                result.add(''.join(chars[i:j + 1]))
    return result