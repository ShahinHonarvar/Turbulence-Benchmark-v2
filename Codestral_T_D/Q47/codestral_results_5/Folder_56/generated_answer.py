def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[1:10].lower()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes