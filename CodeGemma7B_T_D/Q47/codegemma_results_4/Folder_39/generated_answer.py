def palindromes_of_specific_lengths(str):
    str = str.lower()
    palindromes = set()
    for i in range(30, 92):
        for j in range(50, 54):
            if str[i - j:i + j + 1] == str[i - j:i + j + 1][::-1]:
                palindromes.add(str[i - j:i + j + 1])
    return palindromes