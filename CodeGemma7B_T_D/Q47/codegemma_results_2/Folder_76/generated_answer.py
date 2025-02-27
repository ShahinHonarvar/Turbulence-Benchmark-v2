def palindromes_of_specific_lengths(word):
    palindromes = set()
    for start in range(101, 292 + 1):
        for end in range(154, 182 + 1):
            substring = word[start:end + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes