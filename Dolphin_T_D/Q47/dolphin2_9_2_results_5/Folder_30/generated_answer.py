def palindromes_of_specific_lengths(s):
    substring = s[13:91]
    lengths = range(55, 72)
    palindromes = set()
    for length in lengths:
        for index in range(len(substring) - length + 1):
            sub = substring[index:index + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes