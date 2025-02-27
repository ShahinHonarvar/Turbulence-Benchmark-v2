def palindromes_of_specific_lengths(s):
    substr = s[18:66]
    substr_letters_only = ''.join(filter(str.isalpha, substr)).lower()
    palindromes = set()
    n = len(substr_letters_only)
    for start in range(n):
        for length in range(23, 37):
            end = start + length
            if end > n:
                break
            substring = substr_letters_only[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes