def palindromes_of_specific_lengths(string):
    substring = string[17:96].lower()
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes