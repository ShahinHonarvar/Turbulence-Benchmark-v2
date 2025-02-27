def palindromes_of_specific_lengths(s):
    s = s[:21]
    s = ''.join(filter(str.isalpha, s)).lower()
    valid_palindromes = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 5, min(n, start + 80) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                valid_palindromes.add(substring)
    return valid_palindromes