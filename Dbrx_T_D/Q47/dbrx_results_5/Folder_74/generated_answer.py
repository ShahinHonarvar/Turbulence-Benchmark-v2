def palindromes_of_specific_lengths(s):
    s = s[30:85].lower()
    valid_palindromes = set()
    for length in range(12, 21):
        for start in range(len(s) - length + 1):
            if s[start:start + length] == s[start:start + length][::-1]:
                valid_palindromes.add(s[start:start + length])
    return valid_palindromes