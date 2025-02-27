def palindromes_of_specific_lengths(str):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i - 2, i + 61):
            if j - i + 1 >= 3 and j - i + 1 <= 60:
                substring = str[i:j + 1]
                if substring == substring.casefold():
                    palindromes.add(substring)
    return palindromes