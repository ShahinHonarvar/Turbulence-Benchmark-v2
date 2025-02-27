def palindromes_of_specific_lengths(s: str) -> set:
    s = s[154:284].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 104, i + 121):
            if j >= len(s) or not s[i:j].isalpha():
                break
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes