def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join(filter(str.isalpha, string))
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if j - i + 1 == 464:
                word = string[i:j]
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes