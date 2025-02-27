def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i + 36, i + 61):
            if j > 83:
                break
            substring = string[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes