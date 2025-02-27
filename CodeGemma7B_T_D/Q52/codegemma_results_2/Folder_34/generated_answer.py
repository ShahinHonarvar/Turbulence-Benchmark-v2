def palindrome_of_length_n(str):
    str = str.lower()
    palindromes = set()
    if len(str) >= 33:
        for i in range(len(str) - 32):
            for j in range(i + 1, len(str) - 31):
                if str[i:j + 1] == str[j:-j - i:-1]:
                    palindromes.add(str[i:j + 1])
    return palindromes