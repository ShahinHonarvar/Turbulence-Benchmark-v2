def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindromes = set()
    for i in range(len(str) - 143):
        for j in range(i + 144, len(str)):
            if str[i] == str[j] and str[i + 1] == str[j - 1] and (str[i + 2] == str[j - 2]):
                palindromes.add(str[i:j + 1])
    return palindromes