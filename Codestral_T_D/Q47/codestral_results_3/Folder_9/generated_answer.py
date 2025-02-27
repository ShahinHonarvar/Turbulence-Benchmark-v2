def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 50, i + 61):
            if j > len(s):
                break
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes