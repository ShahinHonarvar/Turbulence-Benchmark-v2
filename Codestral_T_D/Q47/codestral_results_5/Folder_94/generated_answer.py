def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[40:95]
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes