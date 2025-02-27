def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:301].lower()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes