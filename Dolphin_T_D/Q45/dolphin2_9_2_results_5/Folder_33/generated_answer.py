def palindromes_between_indices(s):
    chars = [c for c in s[7:10] if c.isalpha()]
    result = set()
    for i in range(len(chars)):
        for j in range(i + 3, len(chars)):
            if chars[i].lower() == chars[j].lower() and (chars[i + 1].lower() == chars[j - 1].lower() if i < j - 1 else True):
                result.add(''.join([chars[x].lower() for x in range(i, j + 1)]))
    return result