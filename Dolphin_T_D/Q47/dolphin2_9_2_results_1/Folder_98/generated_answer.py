def palindromes_of_specific_lengths(s):
    substring = s[:21]
    requirement = substring.lower()
    palindromes = set()
    for length in range(5, 81):
        for index in range(0, 21 - length + 1):
            sub = requirement[index:index + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes