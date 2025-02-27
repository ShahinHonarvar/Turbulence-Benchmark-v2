def palindromes_of_specific_lengths(s):
    string = s[63:71]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j]
            lower_substring = substring.lower()
            if len(lower_substring) in range(4, 6) and lower_substring == lower_substring[::-1]:
                palindromes.add(substring)
    return palindromes