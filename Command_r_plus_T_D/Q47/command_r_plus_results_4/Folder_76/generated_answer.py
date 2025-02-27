def palindromes_of_specific_lengths(s: str) -> set:
    s = s[100:293].lower()
    palindromes = set()
    for i in range(len(s) - 154):
        for length in range(154, 183):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes