def palindromes_of_specific_lengths(string):
    string = string[0:301]
    palindromes = set()
    for length in range(50, 61):
        for i in range(301 - length + 1):
            sub = string[i:i + length]
            if sub == sub.lower():
                palindromes.add(sub)
    return palindromes