def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(41, 90):
        for j in range(23, 39):
            if i + j <= 90:
                substring = string[i:i + j]
                if substring.lower() == substring[::-1].lower() and substring.isalpha():
                    palindromes.add(substring)
    return palindromes