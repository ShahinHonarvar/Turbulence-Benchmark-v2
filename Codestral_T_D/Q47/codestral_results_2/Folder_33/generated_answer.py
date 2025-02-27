def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[130:296]
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower():
                if sub.isalpha():
                    palindromes.add(sub)
    return palindromes