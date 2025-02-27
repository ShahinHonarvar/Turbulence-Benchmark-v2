def palindromes_of_specific_lengths(s: str) -> set:
    s = s[1:300].lower()
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes