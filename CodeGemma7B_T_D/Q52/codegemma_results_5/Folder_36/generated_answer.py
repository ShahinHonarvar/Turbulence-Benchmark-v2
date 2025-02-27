from string import ascii_lowercase

def palindrome_of_length_n(text):
    smalltext = text.lower()
    palindromes = set()
    for i in range(len(smalltext) - 1):
        for j in range(i + 1, len(smalltext)):
            for k in range(j + 1, len(smalltext)):
                substring = smalltext[i:k + 1]
                if substring == substring[::-1] and len(substring) == 338:
                    palindromes.add(text[i:k + 1])
    return palindromes