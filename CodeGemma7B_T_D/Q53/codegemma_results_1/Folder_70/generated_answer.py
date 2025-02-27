def palindrome_of_length_at_least_n(str):
    palindromes = set()
    str = str.lower()
    for i in range(len(str)):
        for j in range(i + 11, len(str) + 1):
            if str[i:j] == str[i:j][::-1]:
                palindromes.add(str[i:j])
    return palindromes