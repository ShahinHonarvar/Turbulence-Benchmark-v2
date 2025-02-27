def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(45, 99):
        for j in range(40, 48):
            if i - j + 1 >= 45 and i + 1 <= 99:
                substring = string[i - j + 1:i + 1]
                if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes