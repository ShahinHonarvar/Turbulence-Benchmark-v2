def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(12, 57):
        for j in range(i - 20, i + 1):
            if j >= 0 and j <= len(string) - 1 and (0 <= i - j <= 21) and (string[j:i + 1] == string[j:i + 1][::-1]):
                palindromes.add(string[j:i + 1])
    return palindromes