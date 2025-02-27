def palindromes_of_specific_lengths(s):
    result = set()
    s = s[127:289].lower()
    letters_only = ''.join(filter(str.isalpha, s))
    n = len(letters_only)
    for length in range(119, 142):
        for start in range(n - length + 1):
            substring = letters_only[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result