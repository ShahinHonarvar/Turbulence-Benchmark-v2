def palindromes_of_specific_lengths(a_string):
    palindromes = set()
    sub_string = a_string[24:85]
    for length in range(21, 32):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length]
            sub = ''.join(filter(str.isalpha, sub))
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes