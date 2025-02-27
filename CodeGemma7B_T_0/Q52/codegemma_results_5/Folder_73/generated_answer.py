def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    if text[i:l + 1] == text[i:l + 1][::-1]:
                        palindromes.add(text[i:l + 1])
    return palindromes