def palindromes_of_specific_lengths(s: str) -> set:
    s = s[1:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for length in [3, 4]:
            if i + length <= len(s) and s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes