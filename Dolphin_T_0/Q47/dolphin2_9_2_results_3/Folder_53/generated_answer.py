def palindromes_of_specific_lengths(string):
    substring = string[1:300]
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes