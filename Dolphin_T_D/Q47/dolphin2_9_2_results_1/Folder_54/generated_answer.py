def palindromes_of_specific_lengths(s):
    to_check = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(to_check) - length + 1):
            substring = to_check[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes