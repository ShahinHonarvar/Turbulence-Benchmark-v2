def palindromes_between_indices(string):
    letters = []
    for i in range(6, 9):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    palindromes = set()
    if len(letters) >= 4:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    for l in range(k + 1, len(letters)):
                        palindrome = letters[i] + letters[j] + letters[k] + letters[l]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes