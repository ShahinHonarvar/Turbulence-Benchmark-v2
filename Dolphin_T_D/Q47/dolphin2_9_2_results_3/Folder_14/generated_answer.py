def palindromes_of_specific_lengths(s):
    s = s[10:75]
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(s) - length + 1):
            if len(s[i:i + length]) == length:
                substring = s[i:i + length]
                if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes