def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[:101].lower()
    palindromes = set()
    for length in range(3, 16):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes