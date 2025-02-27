def palindromes_of_specific_lengths(s: str) -> set:
    s = s[:21].lower()
    palindromes = set()
    for length in range(5, 81):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes