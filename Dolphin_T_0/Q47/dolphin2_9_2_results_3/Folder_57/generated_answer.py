def palindromes_of_specific_lengths(s):
    result = set()
    s = s[15:95]
    for length in range(39, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in substring)) and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result