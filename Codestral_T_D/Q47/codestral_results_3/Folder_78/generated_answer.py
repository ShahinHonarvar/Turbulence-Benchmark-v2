def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(19, 56):
            if i + j > len(s):
                break
            substring = s[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes