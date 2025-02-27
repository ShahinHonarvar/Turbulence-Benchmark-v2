def palindromes_of_specific_lengths(s: str) -> set:
    s = s[154:284].lower()
    palindromes = set()
    for i in range(len(s) - 104):
        for j in range(104, 121):
            substring = s[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes