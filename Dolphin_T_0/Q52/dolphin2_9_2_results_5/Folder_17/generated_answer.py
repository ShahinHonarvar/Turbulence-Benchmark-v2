def palindrome_of_length_n(str):
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i, min(i + 289, len(str))):
            if str[i:j + 1] == str[i:j + 1][::-1]:
                palindromes.add(str[i:j + 1])
    return palindromes