def palindromes_of_specific_lengths(strng):
    strng = strng.lower()
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, min(i + 7, 9) + 1):
            substring = strng[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes