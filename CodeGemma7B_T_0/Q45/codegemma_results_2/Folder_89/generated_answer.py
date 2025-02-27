def palindromes_between_indices(text):
    text = text.lower()
    letters = [char for char in text[5:10] if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        palindrome = ''.join(letters[i:m + 1])
                        if len(palindrome) >= 6:
                            palindromes.add(palindrome)
    return palindromes