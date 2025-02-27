def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 56):
        for j in range(97, 123):
            if i <= len(string) - 57 and string[i:i + 57].lower().count(chr(j)) == 57:
                palindromes.add(string[i:i + 57])
    return palindromes